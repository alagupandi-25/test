#include <DHT.h>
#include <DHT_U.h>

#include <WiFi.h>
#include <HTTPClient.h>

#define DHTPIN 4
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

char* ssid = "*********";         
char* password = "*********";    
String server = "http://api.thingspeak.com/update"    
String apikey = "*********";     

void setup() {
  Serial.begin(9600);
  dht.begin();
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.println("Connecting to WiFi...");
    delay(1000);
  }
  Serial.println("WiFi connected!");
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    String url = server + "?apikey=" + apikey + "&field1=" + String(t) + "&field2=" + String(h);
    http.begin(url);
    int statusCode = http.GET();
    if (statusCode > 0) {
      String payload = http.getString();
      Serial.println("Response: " + payload);
    } else {
      Serial.println("Error: " + String(statusCode));
    }t
    http.end();
  } else {
    Serial.println("WiFi not connected. Unable to send data.");
  }
  delay(2000);
}
