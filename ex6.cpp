#include <DHT.h>
#include <BluetoothSerial.h>

#define DHTPIN 4       
#define DHTTYPE DHT11     

DHT dht(DHTPIN, DHTTYPE);

BluetoothSerial SerialBT;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32_DHT11"); 
  Serial.println("The device started, now you can pair it with Bluetooth");
  dht.begin();
}

void loop() {
  delay(2000);

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();        

  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.print(" °C, Humidity: ");
  Serial.print(humidity);
  Serial.println(" %");
  
  SerialBT.print("Temperature: ");
  SerialBT.print(temperature);
  SerialBT.print(" °C, Humidity: ");
  SerialBT.print(humidity);
  SerialBT.println(" %");
}
