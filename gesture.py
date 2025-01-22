




import cv2
import mediapipe as mp
import serial
import time

# Set up serial communication with Arduino
ser = serial.Serial('COM3', 9600)  # Replace with your Arduino's COM port
time.sleep(2)  # Wait for Arduino to initialize

# Initialize MediaPipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize OpenCV window
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # Flip the frame for a mirror view
    frame = cv2.flip(frame, 1)
    
    # Process the frame with MediaPipe hands
    results = hands.process(frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Extract wrist and finger positions (for gestures)
            wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
            thumb = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Calculate Y-coordinate of wrist to detect up/down movement
            wrist_y = wrist.y

            # Gesture detection logic:
            # Check if the hand is up or down based on wrist Y position
            if wrist_y < 0.4:  # Hand is raised
                ser.write(b'U')  # Send 'U' to move shoulder up
            elif wrist_y > 0.6:  # Hand is lowered
                ser.write(b'D')  # Send 'D' to move shoulder down
            else:
                # Default neutral state: shoulder stays in the middle
                pass

            # Check if the thumb is moving right or left for base control
            if thumb.x > index_finger.x:  # Thumb is to the right
                ser.write(b'L')  # Send 'L' to move base left
            elif thumb.x < index_finger.x:  # Thumb is to the left
                ser.write(b'R')  # Send 'R' to move base right

            # Check if thumb and index finger are spread for gripper open
            if abs(thumb.x - index_finger.x) > 0.1:
                ser.write(b'O')  # Send 'O' to open gripper
            else:
                ser.write(b'C')  # Send 'C' to close gripper

            # Draw landmarks on the frame (optional for debugging)
            mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display the frame
    cv2.imshow("Gesture Controlled Arm", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()


