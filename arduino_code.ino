#include <Servo.h>

Servo baseServo;
Servo shoulderServo;
Servo elbowServo;
Servo gripperServo;

char command;

void setup() {
    Serial.begin(9600);
    
    // Attach servos to their respective PWM pins
    baseServo.attach(9);     // Base servo (left/right)
    shoulderServo.attach(10); // Shoulder servo (up/down)
    elbowServo.attach(11);    // Elbow servo
    gripperServo.attach(12);  // Gripper servo (open/close)
    
    // Initialize servos to their neutral positions
    baseServo.write(90);      // Base at center position
    shoulderServo.write(90);  // Shoulder at neutral position
    elbowServo.write(90);     // Elbow at neutral position
    gripperServo.write(90);   // Gripper open (neutral position)
}

void loop() {
    if (Serial.available() > 0) {
        command = Serial.read();  // Read the incoming command

        switch (command) {
            case 'L': 
                baseServo.write(180);  // Move base to the left (90° -> 180°)
                break;
                
            case 'R': 
                baseServo.write(0);    // Move base to the right (90° -> 0°)
                break;
                
            case 'U': 
                shoulderServo.write(45);  // Move shoulder up (adjust angle if needed)
                elbowServo.write(45);     // Adjust elbow position for up movement
                break;
                
            case 'D': 
                shoulderServo.write(135); // Move shoulder down (adjust angle if needed)
                elbowServo.write(135);    // Adjust elbow position for down movement
                break;
                
            case 'O': 
                gripperServo.write(0);   // Open gripper (adjust as per servo)
                break;
                
            case 'C': 
                gripperServo.write(90);  // Close gripper (adjust as per servo)
                break;
                
            default:
                // Default behavior for unrecognized commands (optional)
                baseServo.write(90);      // Reset base to neutral position
                shoulderServo.write(90);  // Reset shoulder to neutral position
                elbowServo.write(90);     // Reset elbow to neutral position
                gripperServo.write(90);   // Reset gripper to open position
                break;
        }
    }
}
