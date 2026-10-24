
const int RAIN_SENSOR = 2;
const int MOTOR_IN1 = 8;
const int MOTOR_IN2 = 9;

// Example settings: apne circuit ke according verify karna.
const bool RAIN_ACTIVE_LOW = true;

void stopMotor() {
  digitalWrite(MOTOR_IN1, LOW);
  digitalWrite(MOTOR_IN2, LOW);
}

bool isRaining() {
  int value = digitalRead(RAIN_SENSOR);
  return RAIN_ACTIVE_LOW ? value == LOW : value == HIGH;
}

void setup() {
  Serial.begin(9600);

  pinMode(RAIN_SENSOR, INPUT);
  pinMode(MOTOR_IN1, OUTPUT);
  pinMode(MOTOR_IN2, OUTPUT);

  stopMotor();
  Serial.println("Automatic Clothes Protection System Started");
}

void loop() {
  if (isRaining()) {
    Serial.println("Rain detected! Moving rack towards shelter.");

    digitalWrite(MOTOR_IN1, HIGH);
    digitalWrite(MOTOR_IN2, LOW);
    delay(2000);

    stopMotor();
    delay(3000);
  } else {
    stopMotor();
    Serial.println("No rain detected. Rack remains stationary.");
    delay(1000);
  }
}
