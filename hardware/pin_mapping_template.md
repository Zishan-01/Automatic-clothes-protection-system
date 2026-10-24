
# Hardware Components and Pin Mapping

## Components
- Arduino board
- Rain sensor module
- Motor driver
- DC motor
- Connecting wires
- Power supply
- Clothes rack mechanism

## Example Pin Mapping

| Component | Arduino Pin |
|---|---|
| Rain sensor digital output | D2 |
| Motor driver IN1 | D8 |
| Motor driver IN2 | D9 |

**Important:** These are example pins. Verify the actual circuit connections before operating hardware.

## Safety Notes
- Never connect a motor directly to an Arduino GPIO pin.
- Use a suitable motor driver and power supply.
- Protect the electronics from moisture.
- Test motor direction and sensor readings before operating the complete mechanism.
