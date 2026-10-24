"""ESP32 MicroPython starter template — hardware configuration required.

IMPORTANT:
- This is a template, not plug-and-play hardware code.
- Set GPIO pins and sensor polarity to match your real circuit.
- Use a suitable motor driver; never power a motor directly from a GPIO.
- Timed movement is only a demonstration. Use limit switches/position feedback
  and emergency-stop logic for a real mechanical installation.
"""

from machine import Pin
from time import sleep

# TODO: Replace these example GPIOs with pins verified for your ESP32 board.
RAIN_SENSOR_PIN = 27
MOTOR_IN1_PIN = 25
MOTOR_IN2_PIN = 26

# Set True if your sensor's digital output goes LOW when rain is detected.
RAIN_ACTIVE_LOW = True

# Example movement duration only; calibrate carefully for your mechanism.
MOVE_SECONDS = 2.0
POLL_SECONDS = 0.5
RETURN_TO_DRYING_AREA_WHEN_DRY = True

rain_sensor = Pin(RAIN_SENSOR_PIN, Pin.IN)
motor_in1 = Pin(MOTOR_IN1_PIN, Pin.OUT)
motor_in2 = Pin(MOTOR_IN2_PIN, Pin.OUT)


def stop_motor():
    """Stop the motor driver inputs. Confirm this behaviour for your driver."""
    motor_in1.value(0)
    motor_in2.value(0)


def move_towards_shelter():
    """Example direction; verify motor direction and driver wiring first."""
    print("Moving rack towards shelter...")
    motor_in1.value(1)
    motor_in2.value(0)
    sleep(MOVE_SECONDS)
    stop_motor()
    print("Timed movement complete. Verify actual rack position.")


def move_towards_drying_area():
    """Example reverse direction; verify motor direction and driver wiring."""
    print("Moving rack towards drying area...")
    motor_in1.value(0)
    motor_in2.value(1)
    sleep(MOVE_SECONDS)
    stop_motor()
    print("Timed movement complete. Verify actual rack position.")


def rain_detected():
    raw_value = rain_sensor.value()
    if RAIN_ACTIVE_LOW:
        return raw_value == 0
    return raw_value == 1


def main():
    # This template assumes the rack starts in the drying area.
    # Real hardware should determine position with limit switches or feedback.
    rack_is_sheltered = False
    stop_motor()
    print("Automatic Clothes Protection System started.")

    while True:
        raining = rain_detected()
        print("Rain detected." if raining else "No rain detected.")

        if raining and not rack_is_sheltered:
            move_towards_shelter()
            rack_is_sheltered = True

        elif (
            not raining
            and rack_is_sheltered
            and RETURN_TO_DRYING_AREA_WHEN_DRY
        ):
            move_towards_drying_area()
            rack_is_sheltered = False

        sleep(POLL_SECONDS)


try:
    main()
except KeyboardInterrupt:
    stop_motor()
    print("Stopped.")
