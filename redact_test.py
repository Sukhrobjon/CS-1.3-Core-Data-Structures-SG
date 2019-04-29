from redact_problem import Redact
import unittest

class RedactTest(unittest.TestCase):

    def test_with_empty_banned_words(self):
        redact_obj = Redact()
        words = ["Hi", "how", "are", "you"]
        banned_words = []
        assert redact_obj.redact_words(words, banned_words) == ["Hi", "how", "are", "you"]

    # def test_two(self):
    #     pass


if __name__ == "__main__":
    unittest.main()
