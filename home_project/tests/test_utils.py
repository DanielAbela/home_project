from unittest import TestCase, mock
from unittest.mock import Mock, patch, mock_open

from utils import check_if_float, round_data, read_file


class TestUtils(TestCase):
    def test_check_if_float_returns_true(self):
        self.assertTrue(check_if_float("456.456"))

    def test_check_if_float_returns_false(self):
        self.assertFalse(check_if_float("test string"))

    def test_round_data(self):
        mock_df = Mock()
        round_data(mock_df, round_value=6)
        mock_df.round.assert_called_with(6)

    def test_read_file(self):
        with patch("builtins.open", mock_open(read_data="data")) as mock_file:
            read_file("path/to/open", mode="test_mode")
            mock_file.assert_called_with("path/to/open", "test_mode")
