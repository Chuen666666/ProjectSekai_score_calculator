import unittest
from unittest.mock import patch

from main import count_score, nonnegative_input


class ScoreCalculatorTests(unittest.TestCase):
    @patch('builtins.input', side_effect=['invalid', '-1', '7'])
    @patch('builtins.print')
    def test_nonnegative_input_retries_until_valid(self, mock_print, mock_input):
        self.assertEqual(nonnegative_input('prompt'), 7)
        self.assertEqual(mock_input.call_count, 3)
        self.assertEqual(mock_print.call_count, 2)

    @patch('builtins.input', side_effect=['2', '1', '3', '4', '5', '999'])
    def test_count_score_calculates_score_health_and_combo(self, mock_input):
        self.assertEqual(count_score('player'), (11, 2, 400, 999))
        self.assertEqual(mock_input.call_count, 6)


if __name__ == '__main__':
    unittest.main()
