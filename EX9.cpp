#include <WiFi.h>

const char* ssid = "your_wifi_ssid"; 
const char* password = "your_wifi_password"; 

const char* server_ip = "RPI_IP_ADDRESS";  
const int server_port = 8080;  

WiFiClient client;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  if (client.connect(server_ip, server_port)) {
    Serial.println("Connected to server");
  } 
  else {
    Serial.println("Connection failed");
  }
}

void loop() {
    client.println("Hello from ESP32!");
    if (client.available()) {
        String response = client.readStringUntil('\n');
        Serial.println("Server response: " + response);
    }
}
