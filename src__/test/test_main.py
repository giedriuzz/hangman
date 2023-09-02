"""Module fot testing database main module"""
import unittest

from main import Letter, Words


class TestsSqlDatabase(unittest.TestCase):
    """Test class for SqlDatabase"""

    def setUp(self):
        """Set up for tests"""
        self.word = Words(word="DOG")
        self.letter = Letter(word=self.word, letter="O")

    def test_is_letter_in_word(self):
        """Test for is_letter_in_word method"""

        self.assertTrue(self.letter.is_letter_in_word(), "O")

    def test_inspect_letter_unused(self):
        """Test for inspect_letter method"""
        result = self.letter.inspect_letters()
        self.assertTrue(result)

    def test_inspect_letter_used(self):
        """Test for inspect_letter method"""

        Letter.MATCHED_LETTERS.append("O")
        result = self.letter.inspect_letters()
        self.assertFalse(result)
        self.assertEqual(self.letter.inspect_letters(), False)

    def test_replace_guessed_letter(self):
        """Test for replace_guessed_letter method"""
        self.letter.create_empty_word_list()
        expected = ["_", "O", "_"]
        result = self.letter.replace_guessed_letter()
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
