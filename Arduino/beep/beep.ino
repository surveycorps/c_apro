// On-Board LED for status indications
int led = 15; // E1

// 3 soft-PWM pins for motor
// Use analogWrite() with arg 0-255
int M1 = 18; // D0
int M2 = 19; // D1
int M3 = 14; // E0

// 3 Analog pins for direction of motors
// maybe you can use digitalWrite???
int dir1 = A0; // A1
int dir2 = A1; // A2
int dir3 = A2; // A3

// 6 Inputs for encoders
// use attachInterrupt
int M1L = 2; // C0
int M1R = A3; // A4
int M2L = 3; // C1
int M2R = A4; // A5
int M3L = 7; // B2
int M3R = A5; // A6

void setup() {
  // put your setup code here, to run once:
  //Serial.begin(9600);
  //printf("\nI'm ALIVE\n\r");
  pinMode(led, OUTPUT);
  pinMode(M1, OUTPUT);
  pinMode(M2, OUTPUT);
  pinMode(M3, OUTPUT);
  //pinMode(dir2, OUTPUT);
  digitalWrite(led, HIGH);

}

void loop() {
  // put your main code here, to run repeatedly:
    digitalWrite(M1, HIGH);
    digitalWrite(M2, HIGH);
    digitalWrite(M3, HIGH);
    analogWrite(dir1, 255);
    analogWrite(dir2, 0);
    analogWrite(dir3, 255);
    digitalWrite(led, HIGH);
    delay(1000);
    digitalWrite(M1, HIGH);
    digitalWrite(M2, HIGH);
    digitalWrite(M3, HIGH);
    analogWrite(dir1, 0);
    analogWrite(dir2, 255);
    analogWrite(dir3, 0);
    digitalWrite(led, LOW);
    delay(1000);
    digitalWrite(M1, LOW);
    digitalWrite(M2, LOW);
    digitalWrite(M3, LOW);
    delay(1000);
}
