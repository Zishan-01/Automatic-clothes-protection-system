# Automatic Clothes Protection System (Python)

A starter implementation for the Automatic Clothes Protection System described in the project report.

## Important implementation note

The report describes a rain/moisture sensor, a controller (ESP32 or Arduino), and a motorized mechanism that moves clothes to shelter. It does **not** confirm the exact board, sensor models, motor driver, GPIO pins, or completed hardware test results.

This repository therefore includes:

1. `src/main.py` — a runnable **software simulation** you can test on a normal computer.
2. `src/esp32_micropython.py` — a **MicroPython hardware template** for an ESP32. Configure the GPIO pins and adapt the sensor/motor logic to your actual circuit before using it with hardware.
3. Unit tests for the simulated control logic.

The computer simulation does not operate physical hardware. The ESP32 template requires MicroPython installed on a compatible board and wiring that matches your configuration.

## System behaviour

- Read whether rain is detected.
- If rain is detected while the rack is in the drying area, request movement to the sheltered position.
- When rain is no longer detected, optionally request a return to the drying area.
- Prevent duplicate movement commands when the rack is already at the requested position.
- Print status messages for testing.

## Project structure

```text
automatic-clothes-protection-system/
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── esp32_micropython.py
├── tests/
│   └── test_controller.py
├── hardware/
│   └── pin_mapping_template.md
├── images/
│   └── .gitkeep
├── report/
│   └── .gitkeep
└── .gitignore
```

## Run the computer simulation

Python 3.10 or newer is recommended. No third-party packages are needed.

```bash
python src/main.py
```

Choose the simulated rain state when prompted. Type `rain`, `dry`, or `quit`.

## Run the tests

```bash
python -m unittest discover -s tests -v
```

## Prepare the ESP32 version

1. Confirm that your board is an ESP32 and that it supports MicroPython.
2. Install a compatible MicroPython firmware and upload `src/esp32_micropython.py`.
3. Update the GPIO pin constants to match your actual wiring.
4. Confirm whether your rain sensor output is digital or analog and adjust the code accordingly.
5. Use a motor driver suitable for your motor. **Do not connect a motor directly to an ESP32 GPIO pin.**
6. Test the sensor and motor separately before enabling automatic operation.
7. Add limit switches or another reliable position feedback mechanism if the rack can travel mechanically. The template uses timed movement only as an example and is not a substitute for position feedback.

## Results and limitations

The simulation demonstrates control flow only. It does not provide measured sensor accuracy, motor response time, reliability, or proof of successful hardware operation. Record those values only after testing the real prototype.

## Before publishing to GitHub

- Replace placeholders with your actual board, sensors, motor driver, and pin mapping.
- Add real prototype and circuit photographs to `images/`.
- Put a sanitized copy of the report in `report/`; remove student IDs, signatures, and other private information from a public copy.
- Never upload Wi-Fi passwords, API keys, or other secrets.
