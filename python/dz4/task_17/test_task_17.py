from task17 import BaseWallet, RubbleWallet, DollarWallet, EuroWallet
import unittest


class CheckWallet(unittest.TestCase):
    """Класс тестирующий банковские счета"""
    def SetUp(self):
        wallet=BaseWallet()
        rubles=RubbleWallet('X', 300)
        dollars=DollarWallet('Y', 50)
        euro=EuroWallet('Z', 65)

    def test_get(self):
        rubles = RubbleWallet('X', 300)
        dollars = DollarWallet('Y', 50)
        euro = EuroWallet('Z', 65)
        self.assertEqual(rubles.get_name(), 'X')
        self.assertEqual(dollars.get_name(), 'Y')
        self.assertEqual(euro.get_name(), 'Z')
        self.assertEqual(rubles.get_amount(), 300)
        self.assertEqual(dollars.get_amount(), 50)
        self.assertEqual(euro.get_amount(), 65)

    def test_get_base_amount(self):
        rubles = RubbleWallet('X', 300)
        dollars = DollarWallet('Y', 50)
        euro = EuroWallet('Z', 65)
        self.assertEqual(rubles.get_base_amount(), 300)
        self.assertEqual(dollars.get_base_amount(), 3000)
        self.assertEqual(euro.get_base_amount(), 4550)

    def test_add(self):
        self.assertEqual(RubbleWallet("X", 10) + 20, RubbleWallet("X", 30))
        self.assertEqual(RubbleWallet("Y", 20) + DollarWallet("Z", 10), RubbleWallet("Y", 620))
        #self.assertEqual(RubbleWallet("X", 10) += 20, RubbleWallet('X', 30))
        self.assertEqual(20 + RubbleWallet("X", 10), RubbleWallet("X", 30))


    def test_sub(self):
        self.assertEqual(RubbleWallet("X", 30) - 20, RubbleWallet('X', 10))
        self.assertEqual(RubbleWallet("X", 1000) - DollarWallet("Y", 10), RubbleWallet("X", 400))

    def test_mul(self):
        self.assertEqual(RubbleWallet("X", 10) * 10, RubbleWallet('X', 100))
        self.assertEqual(DollarWallet("Y", 3) * 10, DollarWallet('Y', 30))

    def test_div(self):
        self.assertEqual(RubbleWallet("X", 10) / 2, RubbleWallet("X", 5))

    #def test_str(self):
        #self.assertEqual(str(RubbleWallet('X', 10)),'Rubble Wallet X 10')

if __name__ == '__main__':
    unittest.main()
