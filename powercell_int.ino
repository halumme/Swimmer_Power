#include "HX711.h"
// This scetch reads analog values of a strain cell through a HX711 bridge
// Arduino reads the data asynchronously, and sends the data to the serial port
// A complementing Python script takes care of the plotting and reporting of the data. 
// 30.10. 2019 added temperature correction, which uses HX711 channel B for temp measurement
// HX711.DOUT  - pin #A1
// HX711.PD_SCK - pin #A0

HX711 scale(A1, A0);    // parameter "gain" is omitted; the default value 128 is used by the library
int Stop_Pin = 2;       // D2 input connected to the Stop button
int Stop = 1;      // 1 equals to false (button not pressed, pullup high)
float slope = 0.2395;   // entinen arvo 0.22237, korjattu 20.11.2019
float tempcor = 0;
float cell = 0;
float temp = 0;

void setup() {
  pinMode(Stop_Pin, INPUT_PULLUP);
  Serial.begin(38400);
}

float Read_Cell(){
  return (scale.read_average(4));  // 4 reading average
}

float Read_Temp() {
  scale.set_gain(32); 	// gain 32 is coupled with channel B (temperature probe)
  temp = scale.read_average(4);
  scale.set_gain(128); 	// gain 128 is coupled with channel A (strain cell)
  return temp;
}

void loop() {
	 Stop = digitalRead(Stop_Pin);	// Monitor status of Stop button
	 if (Stop == 0) {		// Stop button has been pressed
		Serial.println("QQQ");	// Python script interpretes this token as finish  
		tempcor = 440000 /((1862000 - Read_Temp())*slope);  // read a new temperature value each time button is pressed
	 } else {
		cell = Read_Cell() * tempcor; // compensates for the temperature dependence of strain cell
		Serial.println(cell);
	 }
 }