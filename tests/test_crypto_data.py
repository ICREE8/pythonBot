import unittest
import crypto_data

class TestCryptoData(unittest.TestCase):
    def test_get_crypto_data(self):
        data = crypto_data.get_crypto_data()
        self.assertIn('bitcoin', data)
        self.assertIn('ethereum', data)

if __name__ == '__main__':
    unittest.main()
