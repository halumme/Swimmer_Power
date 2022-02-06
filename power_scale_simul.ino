// # include "HX711.h"
// This sketch simulates an Arduino reading a strain gauge
// It is used in testing of the plotting software (a Python script).
// After a reset it waits for 10 sec, after which it prints measurement data to the serial line.
// Maximum reading is about 750000 units at 30 seconds after the start of printing
// The reading frequency is set by the variable 'space'

float v = 0;
float x = 0;
long t = 0;
float space = 350; // Spacing of readings in milliseconds

void setup() {
  Serial.begin(38400);
}

void loop() {
  while (millis()<10000) {
     if (millis()-t > vali){
       t= millis();
       Serial.println(x);
     }
  }
  while (x<40){
    if (millis()-t > space){
      t= millis();
      v = -833 * x * x + 50000 * x;
      x = x + space/1000;
      Serial.println(v);
    }
  }
  Serial.println("EOD");  // indicates end of data (any non-numeric string will do)
  while (1) {
    delay(1000);
  }
}
