#include <Servo.h>

Servo s1;
int press_angle = 90;
int release_angle = 0;

void setup() {
    s1.attach(9);
    Serial.begin(9600);
}

void press_button() {
  s1.write(press_angle);
  delay(500);
  s1.write(release_angle);
  delay(500);
  Serial.println("completed");
}

void loop() {
    if (Serial.available() > 0) {
        String command = Serial.readStringUntil('\n');
        command.trim();
        Serial.println("Command recieved: " + command);

        if (command == "press") {
            press_button();
        } else if (command == "repress") {
            press_button();
        } else {
            Serial.println("Unknown command");
        }
    }
}
