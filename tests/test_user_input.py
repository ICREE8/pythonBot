import unittest
from unittest.mock import patch
import user_input

class TestUserInput(unittest.TestCase):
    @patch('builtins.input', side_effect=['1000', 'USD'])
    def test_get_user_amount_and_currency(self, mock_input):
        amount, currency = user_input.get_user_amount_and_currency()
        self.assertEqual(amount, 1000)
        self.assertEqual(currency, 'USD')

if __name__ == '__main__':
    unittest.main()
