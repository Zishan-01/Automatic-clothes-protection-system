import unittest

from src.main import ClothesProtectionController, RackPosition


class ControllerTests(unittest.TestCase):
    def test_rain_moves_rack_to_shelter(self):
        controller = ClothesProtectionController()
        message = controller.process_sensor_reading(True)
        self.assertEqual(controller.status.position, RackPosition.SHELTER)
        self.assertIn("moved to shelter", message)

    def test_dry_weather_returns_rack(self):
        controller = ClothesProtectionController()
        controller.process_sensor_reading(True)
        message = controller.process_sensor_reading(False)
        self.assertEqual(controller.status.position, RackPosition.DRYING_AREA)
        self.assertIn("returned to drying area", message)

    def test_repeated_rain_does_not_change_sheltered_position(self):
        controller = ClothesProtectionController()
        controller.process_sensor_reading(True)
        message = controller.process_sensor_reading(True)
        self.assertEqual(controller.status.position, RackPosition.SHELTER)
        self.assertIn("already in shelter", message)

    def test_optional_return_can_be_disabled(self):
        controller = ClothesProtectionController(return_when_dry=False)
        controller.process_sensor_reading(True)
        controller.process_sensor_reading(False)
        self.assertEqual(controller.status.position, RackPosition.SHELTER)


if __name__ == "__main__":
    unittest.main()
