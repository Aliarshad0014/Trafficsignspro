import pygame
import unittest

class TestCar(unittest.TestCase):
   
    def test_car_image(self):
        # Test that the car image loads successfully
        carImg = pygame.image.load('images/car.png')
        self.assertIsNotNone(carImg)

        # Test that the loaded image has the expected dimensions
        expected_width = 64
        expected_height = 64
        self.assertEqual(carImg.get_width(), expected_width)
        self.assertEqual(carImg.get_height(), expected_height)

    def test_ped_and_stop_functions(self):
        pedImg = pygame.Surface((40, 80))
        pedImg.fill((255, 0, 0))
        stopImg = pygame.Surface((80, 160))
        stopImg.fill((255, 255, 255))
        x, y = 0, 0
        x1, y1 = 40, 250

        try:
            # Call the functions being tested
            self.screen.blit(pedImg, (x, y))
            self.screen.blit(stopImg, (x1, y1))
            pygame.display.update()

        except Exception as e:
            self.fail(f"Exception occurred: {e}")

    @classmethod
    def setUpClass(cls):
        pygame.init()
        cls.screen = pygame.display.set_mode((800, 800))

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

