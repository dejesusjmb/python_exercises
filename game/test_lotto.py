import unittest
from lotto import Lotto
from mock import patch


class TestLotto(unittest.TestCase):

    def setUp(self):
        self._game = Lotto()

    @patch('lotto.randint')
    def test__play__return_bet_if_one_number_correct(self, mock_randint):
        mock_randint.side_effect = [1, 2, 3]
        self.assertEquals(self._game.play(1, [1, 4, 5]), 1)
        mock_randint.assert_called_with(1, 10)

    @patch('lotto.randint')
    def test__play__return_five_times_bet_if_two_number_correct(self, mock_randint):
        mock_randint.side_effect = [1, 2, 3]
        self.assertEquals(self._game.play(1, [1, 4, 3]), 5)
        mock_randint.assert_called_with(1, 10)

    @patch('lotto.randint')
    def test__play__return_ten_times_bet_if_all_number_correct(self, mock_randint):
        mock_randint.side_effect = [1, 2, 3]
        self.assertEquals(self._game.play(1, [1, 2, 3]), 10)
        mock_randint.assert_called_with(1, 10)

    @patch('lotto.randint')
    def test__play__return_zero_if_no_number_correct(self, mock_randint):
        mock_randint.side_effect = [1, 2, 3]
        self.assertEquals(self._game.play(1, [4, 5, 6]), 0)
        mock_randint.assert_called_with(1, 10)


if __name__ == "__main__":
    unittest.main()
