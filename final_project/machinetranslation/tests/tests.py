import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertIsNone(english_to_french(None))

    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertIsNone(french_to_english(None))

if __name__ == "__main__":
    unittest.main()