import unittest
import calculations

class TestCalculations(unittest.TestCase):
    def test_calculate_crypto_equivalent(self):
        amount = 1000
        currency = 'USD'
        result = calculations.calculate_crypto_equivalent(amount, currency)
        self.assertIn('BTC', result)
        self.assertIn('ETH', result)

if __name__ == '__main__':
    unittest.main()
