
int buzz=7;
int s=A5;
int st=150;
int distance=0;
int duration=0;
int Mo=6;
int trig=10;
int echo=9;

#include <LiquidCrystal.h>
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs,en,d4,d5,d6,d7);

void setup() 
{
 pinMode(buzz,OUTPUT);
 pinMode(s,INPUT);
 pinMode(trig,OUTPUT);
 pinMode(echo,INPUT);
 pinMode(Mo,OUTPUT);
 lcd.begin(16,2);
 //lcd.print("hallo sss");
 Serial.begin(9600);
}
void loop() 
{
 int analogSensor=analogRead(s);
 Serial.println(analogSensor);

 digitalWrite(trig,HIGH);
 delayMicroseconds(2);
 digitalWrite(trig,LOW);
 delayMicroseconds(10);
 duration=pulseIn(echo,HIGH);
 distance=(duration/2)/29.1;
 Serial.println(distance);
 
 lcd.setCursor(1,0);
 lcd.print("Speed");
  
 //lcd.print(millis() / 50);
 //lcd.scrollDisplayLeft();
 lcd.setCursor(0,1);
 //lcd.print("Speed");
 //delay(150);
 
 if (analogSensor > st)
 {
 //digitalWrite(buzz,HIGH);
 
 tone(buzz,1000);
}
else
{
//digitalWrite(buzz,LOW);
 
 noTone(buzz);
 
}
//delay(100);
if(distance>=24)

 {
  Serial.println("no any vehicle detected");
 digitalWrite(Mo,HIGH);
 digitalWrite(buzz,LOW);
 lcd.print("no any vehicle detected");
 }
 else
 {
 Serial.println("any vehicle detected");
 digitalWrite(Mo,LOW);
 digitalWrite(buzz,LOW);
 lcd.print("any vehicle detected");
 
 }
}
