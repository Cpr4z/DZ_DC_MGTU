import unittest
from task18 import Field

class TestField(unittest.TestCase):
    """Класс тестирующий структуру данных Field"""
    def test_set(self):
        """Тестирование записи в ячейки"""
        field = Field()

        field[1, 'a'] = 25
        self.assertEqual(field[1, 'a'], 25)
        field['a', 1] = 43
        self.assertEqual(field['a', 1], 43)
        field['a', '1'] = 12
        self.assertEqual(field['a', '1'], 12)
        field['1', 'a'] = 65
        self.assertEqual(field['1', 'a'], 65)
        field['1a'] = 123
        self.assertEqual(field['1a'], 123)
        field['a1'] = 87
        self.assertEqual(field['a1'], 87)
        field[1, 'A'] = 90
        self.assertEqual(field[1, 'A'], 90)
        field['A', 1] = 23
        self.assertEqual(field['A', 1], 23)
        field['A', '1'] = 4
        self.assertEqual(field['A', '1'], 4)
        field['1', 'A'] =16
        self.assertEqual(field['1', 'A'], 16)
        field['1A'] = 76
        self.assertEqual(field['1A'], 76)
        field['A1'] = 30
        self.assertEqual(field['A1'], 30)

    def test_wrong_set(self):
        """Функция тестирующая неправильный ввод данных"""
        field = Field()
        try:
            field['AA1'] = 3
        except ValueError:
            self.assertEqual(1, 1)
        else:
            self.assertEqual(1, 2)


    def test_in(self):
        """Тестирование метода наличия поля в структуре"""
        field = Field()

        field[1, 'a'] = 25
        self.assertEqual((1, 'a') in field, True)
        self.assertEqual(('A', '1') in field, True)
        self.assertEqual((4, 'd') in field, False)
        field[4, 'd'] = 4
        self.assertEqual((4, 'd') in field, True)
        self.assertEqual('A1' in field, True)
        self.assertEqual('4D' in field, True)

if __name__ == '__main__':
    unittest.main()