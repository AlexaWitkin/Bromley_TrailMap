/*
RS422.ino
TrailMapInterface V1.0
*/

#include <LedControl.h>

int DIN = 8;
int CS = 9;
int CLK = 10;

LedControl led(DIN, CLK, CS, 0);
byte open[8] = {0x01, 0x03, 0x07, 0x8E, 0xDC, 0xf8, 0x70, 0x20};
byte closed[8] = {0x81, 0xC3, 0x66, 0x3C, 0x18, 0x3C, 0x66, 0xC3};
byte delayed[8] = {0x00, 0x00, 0x3C, 0x3C, 0x3C, 0x3C, 0x00, 0x00};

void setup() {
    // start communication with baud rate 9600
    Serial.begin(9600);

    // wait a moment to allow serial ports to initialize
    delay(100);

    led.shutdown(0, false); // display is in power saving mode on startup
    led.setIntensity(0, 10); // set brightness value
    led.clearDisplay(0); // clear the display
}

void loop() {
    printByte(open);
    delay(1000);
    printByte(closed);
    delay(1000);
    printByte(delayed);
    delay(1000);

    if (Serial.available()) {
        int a = Serial.parseInt(); // will be serial value sent by rasp-pi
        Serial.println(a); // print serial value

        if (a = 100) {
            printByte(open);
        }
        if (a = 200) {
            printByte(delayed);
        }
        if (a = 300) {
            printByte(closed);
        }
    }
}

void printByte(byte type []) {
    for(int i = 0; i < 8; i++)
    {
        led.setRow(0, i, type[i]);
    }
}


/*
make something to save current image, then change each with if statements
based on input recieved from website
*/

// check for which button
// if (serialInput == open) {
//  printByte(open);
// }
// else if (serialInput == closed) {
//   printByte(closed);
// }
// else if (serialInput == delayed) {
//   printByte(delayed);
// }





// Code for Hardware
/*
// Check if there's data available on Serial
if (Serial.available()) {
  int data = Serial.read();  // read the received character
  Serial.print(data);
  Serial.print("");         // echo back the data to the sender
}
*/

// Code for Software Serial

/*
#include <SoftwareSerial.h>

// define the SoftwareSerial object and their pins
SoftwareSerial rs422(6, 7);  // RX: 6, TX: 7

void setup() {
  // start communication with baud rate 9600
  rs422.begin(9600);

  // wait a moment to allow serial ports to initialize
  delay(100);
}

void loop() {
  // Check if there's data available on rs422
  if (rs422.available()) {
    char data = rs422.read();  // read the received character
    rs422.print(data);         // echo back to data to the sender
  }
}
*/
