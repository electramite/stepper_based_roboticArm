#include <Servo.h>
Servo srX;
Servo srY;

void setup() {
  srX.attach(9);
  srY.attach(10);
  Serial.begin(9600);
}

void loop() {
  String data = Serial.readStringUntil('\n');
  int c = 0;
  int d[2]={0};
  int x;
    for(int i=0;i<data.length();i++)
    {
      if(data[i]==' ')
      {
        c++;
      }else
      {
        x = data[i]-48;
        d[c]=d[c]*10 +x;
      }
    }
  srX.write(d[0]);
  srY.write(d[1]);  
}
