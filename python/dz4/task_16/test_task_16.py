from task16 import Calculator
import unittest

class CheckCalculator(unittest.TestCase):
    """Класс тестирущий калькулятор"""

    def setUp(self) -> None:
        self.app = Calculator()

    def test_sum(self):
        self.assertEqual(self.app.sum(5, 2), 7)
        self.assertEqual(self.app.sum(-5,6), 1)
        self.assertEqual(self.app.sum(-5, -4), -9)

    def test_sub(self):
        self.assertEqual(self.app.sub(-5,-5), 0)
        self.assertEqual(self.app.sub(3, 4), -1)
        self.assertEqual(self.app.sub(18, 9), 9)

    def test_mul(self):
        self.assertEqual(self.app.mul(6, 5), 30)
        self.assertEqual(self.app.mul(-6, 6), -36)
        self.assertEqual(self.app.mul(-6, -6), 36)

    def test_div(self):
        self.assertEqual(self.app.div(30, 5), 6.0)
        self.assertEqual(self.app.div(30, 7, True), 2)
        self.assertEqual(self.app.div(30, -5), -6.0)
        self.assertEqual(self.app.div(30, -7, True), -5)

    def test_history(self):
        self.app.div(30, -7, True)
        self.assertEqual(self.app.history(1),'div(30, -7) == -5')

if __name__ == '__main__':
    unittest.main()
