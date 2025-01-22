# Gesture-Controlled Robotic Arm

This project features a gesture-controlled robotic arm using Arduino Uno and MediaPipe for hand tracking. The arm can be controlled with simple hand gestures, making automation more intuitive and interactive.

## Features

- **Gesture Control:** Move the arm left/right and up/down using hand gestures.
- **Gripper Control:** Open and close the gripper by detecting finger movements.
- **Arduino-Based:** Uses Arduino Uno to process commands and control servos.
- **Computer Vision:** Utilizes Python and MediaPipe for real-time hand landmark detection.

## Components Used

- **Hardware:**
  - Arduino Uno
  - Servo Motors
  - Wooden Robotic Arm Structure
  - Webcam
  
- **Software:**
  - Arduino IDE
  - Python (for hand tracking and control)
  - OpenCV
  - MediaPipe

## Installation and Setup

1. Clone the Repository:
   ```bash
   git clone https://github.com/yourusername/gesture-controlled-robotic-arm.git
   cd gesture-controlled-robotic-arm
   ```

2. Install Python Dependencies:
   ```bash
   pip install opencv-python mediapipe
   ```

3. Upload the Code to Arduino:
   - Open the Arduino IDE.
   - Upload the provided sketch to the Arduino Uno.

4. Run the Gesture Recognition Script:
   ```bash
   python hand_tracking.py
   ```

## Usage

- **Move Left/Right:** Gesture left/right to rotate the arm base.
- **Move Up/Down:** Gesture up/down to control the arm's elbow and shoulder.
- **Gripper Control:** Open or close fingers to control the gripper.

## Contributing
Feel free to contribute by submitting issues or pull requests.
---

**Developer:** Mahbub Al Hasan Akib  
**GitHub:** akib-pixel  

---


