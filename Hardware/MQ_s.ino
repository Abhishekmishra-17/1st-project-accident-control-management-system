
int L=1;
int b=10;
int s=A5;
int st=150;

void setup() 
{
 pinMode(b,OUTPUT);
 pinMode(s,INPUT);
 Serial.begin(9600);
}

void loop() 
{
 int analogSensor=analogRead(s);
 Serial.println(analogSensor);
 
 if (analogSensor > st)
 {
 digitalWrite(L,HIGH);
 tone(b,1000,200);
}
else
{
 digitalWrite(L,LOW);
 noTone(b);
}
delay(100);
}
