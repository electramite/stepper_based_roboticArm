#include <Servo.h>
Servo srX;


void setup() {
  srX.attach(9);
  srX.write(0);
  Serial.begin(9600);
  
}

void loop() {
  String data = Serial.readStringUntil('\n');
  int x = data.toInt();
  srX.write((180 - x)); 
}
