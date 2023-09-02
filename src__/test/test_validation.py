"""Module fot testing database validation module"""
import unittest
from unittest.mock import patch

from validation import (
    input_only_email,
    input_only_integer_value_not_bigger,
    return_dict_value_by_key,
)


class TestValidation(unittest.TestCase):
    """Test class for validation module"""

    @patch("builtins.input", return_value="5")
    def test_input_only_integer_value_not_bigger_equal(
        self, mock_input
    ):  # pylint: disable=unused-argument
        """Test for input_only_integer_value_not_bigger method input equal"""
        result = input_only_integer_value_not_bigger(5, "Input: ")
        self.assertEqual(result, 5)

    @patch("builtins.input", return_value="1")
    def test_return_dict_value_by_key(
        self, mock_input
    ):  # pylint: disable=unused-argument
        """Test for return_dict_value_by_key method"""
        result = return_dict_value_by_key(
            5, "input_text", {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
        )
        self.assertEqual(result, "one")

    @patch("builtins.input", return_value="g@g.lt")
    def test_input_only_email(self, mock_input):  # pylint: disable=unused-argument
        """Test for input_only_email method"""
        result = input_only_email("g@g.lt")
        self.assertEqual(result, "g@g.lt")


if __name__ == "__main__":
    unittest.main()
