import unittest
import currency_data

class TestCurrencyData(unittest.TestCase):
    def test_get_inflation_data(self):
        data = currency_data.get_inflation_data()
        self.assertIsInstance(data, dict)

if __name__ == '__main__':
    unittest.main()
