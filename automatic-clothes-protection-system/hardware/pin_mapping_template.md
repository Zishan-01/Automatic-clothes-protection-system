# Hardware and Pin Mapping (Fill in after checking your prototype)

The project report mentions a rain/moisture sensor, a controller, and a motorized mechanism. It does not confirm exact component models or GPIO assignments.

| Function | Actual component/model | Board pin / connection | Verified? |
|---|---|---|---|
| Controller | Fill in | — | No |
| Rain sensor output | Fill in | GPIO ___ | No |
| Motor driver input 1 | Fill in | GPIO ___ | No |
| Motor driver input 2 | Fill in | GPIO ___ | No |
| Motor power supply | Fill in | As specified by motor/driver | No |
| Shelter position limit switch (recommended) | Fill in | GPIO ___ | No |
| Drying-area limit switch (recommended) | Fill in | GPIO ___ | No |

## Safety checklist

- Never connect a motor directly to a microcontroller GPIO.
- Verify voltage/current ratings for the board, sensor, driver, and motor.
- Confirm the sensor's active HIGH/LOW behaviour.
- Test motor direction with the mechanism unloaded.
- Add limit switches/position feedback and a way to stop the mechanism.
- Keep electronics protected from rain and moisture.
