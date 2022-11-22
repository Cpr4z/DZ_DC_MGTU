import unittest
from task19 import Field


class TestField(unittest.TestCase):
    """Класс тестирующий структуру данных Field"""
    def test_set(self):
        """Метод тестирующий запись валидных данных через точечную нотацию"""
        field = Field()
        field.a1 = 25
        self.assertEqual(field.A1, 25)
        field.A4 = 45
        self.assertEqual(field.a4, 45)

    def test_wrong_set(self):
        """Метод тестирующий ввод невалидных данных"""
        field = Field()
        try:
            field.AA1 = 35
        except ValueError:
            self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()