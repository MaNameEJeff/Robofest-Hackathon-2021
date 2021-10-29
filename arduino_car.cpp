#define ena 5 //Assuming it controls LEFT
#define enb 6 //Assuming it controls RIGHT
#define lb 8
#define lf 9
#define rb 10
#define rf 11
#define del 50

int readingL = 0;
int readingR = 0;
double speedL = 0.00;
double speedR = 0.00;

int getDistance(int echoPin, int triggerPin) {

  pinMode(triggerPin, OUTPUT);
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  pinMode(triggerPin, INPUT);
  return pulseIn(echoPin, HIGH);

}

void setup() {
  
  Serial.begin(9600);
  pinMode(ena, OUTPUT);
  pinMode(enb, OUTPUT);
  pinMode(lf, OUTPUT);
  pinMode(lb, OUTPUT);
  pinMode(rf, OUTPUT);
  pinMode(rb, OUTPUT);
  
  analogWrite(ena, 255);
  analogWrite(enb, 255);

  digitalWrite(lf, LOW);
  digitalWrite(lb, LOW);
  digitalWrite(rf, LOW);
  digitalWrite(rb, LOW);

  pinMode(A0, INPUT);
  pinMode(A1, INPUT);

}

void loop() {
  
  if(Serial.available() > 0) {
    char ch = Serial.read();

    if (ch == 'f') {

      double cm = 0.01723 * getDistance(12, 3);
      delay(100);

      readingL = analogRead(A0);
      readingR = analogRead(A1);

      speedL = (double(readingL)/450.00)*255.00;
      speedR = (double(readingR)/450.00)*255.00;

      if (cm <= 20.00) {
        
        Serial.println("Obstacle detected");
        
        digitalWrite(lf, LOW);
        digitalWrite(lb, LOW);
        digitalWrite(rf, LOW);
        digitalWrite(rb, LOW);
        delay(del);

      }

      analogWrite(ena, speedL);
      analogWrite(enb, speedR);
      
      digitalWrite(lf, HIGH);
      digitalWrite(lb, LOW);
      digitalWrite(rf, HIGH);
      digitalWrite(rb, LOW);
      delay(del);
      digitalWrite(lf, LOW);
      digitalWrite(lb, LOW);
      digitalWrite(rf, LOW);
      digitalWrite(rb, LOW);  
    }
  }
}
