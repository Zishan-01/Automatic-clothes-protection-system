"""Computer simulation for the Automatic Clothes Protection System.

This file is safe to run on a normal computer. It simulates sensor readings
and rack movement; it does not control physical hardware.
"""

from dataclasses import dataclass
from enum import Enum


class RackPosition(Enum):
    DRYING_AREA = "drying area"
    SHELTER = "shelter"


@dataclass
class SystemStatus:
    raining: bool = False
    position: RackPosition = RackPosition.DRYING_AREA


class ClothesProtectionController:
    """Simple control logic separated from any specific hardware."""

    def __init__(self, return_when_dry: bool = True) -> None:
        self.status = SystemStatus()
        self.return_when_dry = return_when_dry

    def process_sensor_reading(self, raining: bool) -> str:
        """Update the simulated rain sensor and decide whether to move."""
        self.status.raining = raining

        if raining and self.status.position is RackPosition.DRYING_AREA:
            self._move_to(RackPosition.SHELTER)
            return "Rain detected: rack moved to shelter."

        if (
            not raining
            and self.return_when_dry
            and self.status.position is RackPosition.SHELTER
        ):
            self._move_to(RackPosition.DRYING_AREA)
            return "No rain detected: rack returned to drying area."

        if raining:
            return "Rain detected: rack is already in shelter."
        return f"No rain detected: rack remains in {self.status.position.value}."

    def _move_to(self, target: RackPosition) -> None:
        # Simulation only: replace this with a motor-driver interface
        # when connecting actual hardware.
        self.status.position = target

    def get_status(self) -> str:
        return (
            f"Rain: {'YES' if self.status.raining else 'NO'} | "
            f"Rack position: {self.status.position.value}"
        )


def main() -> None:
    controller = ClothesProtectionController(return_when_dry=True)

    print("=" * 55)
    print(" AUTOMATIC CLOTHES PROTECTION SYSTEM — SIMULATION")
    print("=" * 55)
    print("Commands: rain, dry, status, quit")
    print("Note: This is a computer simulation, not hardware control.")

    while True:
        try:
            command = input("\nEnter command: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting simulation.")
            break

        if command == "quit":
            print("Simulation stopped.")
            break
        elif command == "status":
            print(controller.get_status())
        elif command in {"rain", "dry"}:
            raining = command == "rain"
            print(controller.process_sensor_reading(raining))
            print(controller.get_status())
        else:
            print("Invalid command. Enter rain, dry, status, or quit.")


if __name__ == "__main__":
    main()
