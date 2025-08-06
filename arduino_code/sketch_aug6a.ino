void setup() {
  Serial.begin(115200); // Use a high baud rate for smoother data
}

void loop() {
  int sensorValue = analogRead(A0); // Assuming potentiometer on A0
  Serial.println(sensorValue);
  delay(100); // Slight delay to reduce CPU usage and match plotting speed
}
