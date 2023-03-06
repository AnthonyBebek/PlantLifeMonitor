#include <dht.h>
#define sensorPin A0
#define DHTpin 5
#define WLpin A4
#define SMpin A2
#define lightpin A3
#define STpin A1
#define Waterpin 2

dht DHT;

int Tdh11() {
  int readData = DHT.read11(DHTpin);
  float t = DHT.temperature;
  return t;
}

int Hdh11() {
  int readData = DHT.read11(DHTpin);
  float h = DHT.humidity;
  return h;
}

int SM(){
  int output_value = analogRead(SMpin);
  //output_value = map(output_value,0,875,0,100);
  return output_value;
}

int WL() {
  int sensorValue = analogRead(WLpin);
  //Serial.println(sensorValue);
  int outputValue = map(sensorValue, 0, 450, 0, 255);
  //Serial.println(outputValue);
  return outputValue;
}

char dataString[50] = {0};
int a = 0;
String Data = "";

float lux=0.00,ADC_value=0.0048828125,LDR_value;

float Light (int LDR_value) {
  lux=(250.000000/(ADC_value*LDR_value))-50.000000;
  return lux;
}

double Thermal(int data)
{
  double temp;
  temp = log(10000.0 * ((1024.0 / data - 1)));
  temp = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * temp * temp)) * temp);
  temp = temp - 273.15;
  temp = temp - 3;
  return temp;
}

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(sensorPin, INPUT);
  pinMode(DHTpin, INPUT);
  pinMode(WLpin, INPUT);
  pinMode(SMpin, INPUT);
  pinMode(lightpin, INPUT);
  pinMode(STpin, INPUT);
  pinMode(Waterpin, OUTPUT);
  digitalWrite(Waterpin, HIGH);
}

void loop() {

  if (Serial.available() > 0) {
    String nr = Serial.readStringUntil('\n');
    //delay(500);
    if (nr == "1") {
      Serial.println("-- DEBUG SUPPORT CODES -- ");
      Serial.println("1 - help");
      Serial.println("2 - DH11 Temp");
      Serial.println("3 - DH11 Humidity");
      Serial.println("4 - Lux");
      Serial.println("5 - Soil Temp");
      Serial.println("6 - Soil Moisture");
      Serial.println("7 - Water Level");
      Serial.println("8 - Pump Off");
      Serial.println("9 - Pump On");
    }
    if (nr == "2") {
      Serial.println(Tdh11());
    }
    if (nr == "3") {
      Serial.println(Hdh11());
    }
    if (nr == "4") {
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.println(Light(analogRead(lightpin)));
    }
    if (nr == "5"){ 
      Serial.println(Thermal(analogRead(STpin)));
    }
    if (nr == "6") {
      Serial.println(SM());
    }
    if (nr == "7") {
      Serial.println(WL());
    }
    if (nr == "8"){
      digitalWrite(Waterpin, HIGH);
      Serial.println("Ok");
    }
    if (nr == "9"){
      digitalWrite(Waterpin, LOW);
      Serial.println("Ok");
    }
  }
}
