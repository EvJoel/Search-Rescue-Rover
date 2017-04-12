#include <Servo.h>
//#include  <String.h>

Servo r_motor;
Servo l_motor;

int r_motor_pin = 7;
int l_motor_pin = 6;


void setup() {
  // put your setup code here, to run once:
  SerialUSB.begin(9600);
}

void loop() {
  int message = readData();
  SerialUSB.print("Message was: ");
  SerialUSB.println(message);
  delay(1000);
  if (message == 48) {
    moveBackward();
    delay(1000);

  }
  if (message == 49) {
    //Serial.println('11');
    moveForward();
    delay(1000);
  }
  if (message == 50) {
    moveLeft();
    delay(1000);
  }
  if (message == 51) {
    moveRight();
    delay(1000);
  }
  if (message == 52) {
    moveStop();
    delay(1000);
  }
  else {
    //Serial.println("no message received");
  }
}


void attachServos() {
  r_motor.attach(r_motor_pin);
  l_motor.attach(l_motor_pin);

}

void moveBackward() {

  r_motor.write(1200);
  l_motor.write(1200);
}

void moveRight() {
  r_motor.write(1800);
  l_motor.write(1200);
}
void moveLeft() {
  r_motor.write(1200);
  l_motor.write(1800);
}
void moveStop() {
  r_motor.write(1500);
  l_motor.write(1500);
}

void moveForward() {
  r_motor.write(1800);
  l_motor.write(1800);
}

int readData() {
  if ( Serial.available() > 0) {
    int message = SerialUSB.read();
    //Serial.println(message);
    return message;
  }


}

