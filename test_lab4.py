import unittest
from Lab4 import Letter, Word, Punctuation, Sentence, Text, TextProcessor


class TestTextClasses(unittest.TestCase):

    def test_letter(self):
        l = Letter("a")
        self.assertEqual(str(l), "a")

    def test_word(self):
        w = Word([Letter(c) for c in "hello"])
        self.assertEqual(str(w), "hello")
        self.assertEqual(w.length(), 5)

    def test_word_equality(self):
        w1 = Word([Letter(c) for c in "test"])
        w2 = Word([Letter(c) for c in "test"])
        w3 = Word([Letter(c) for c in "best"])

        self.assertEqual(w1, w2)
        self.assertNotEqual(w1, w3)

    def test_vowel_count(self):
        w = Word([Letter(c) for c in "hello"])
        self.assertEqual(w.vowel_count(), 2)

    def test_punctuation(self):
        p = Punctuation("!")
        self.assertEqual(str(p), "!")

    def test_sentence_repr(self):
        s = Sentence([
            Word([Letter(c) for c in "Hello"]),
            Word([Letter(c) for c in "world"]),
            Punctuation("!")
        ])
        self.assertEqual(str(s), "Hello world!")

    def test_text_cleaning(self):
        processor = TextProcessor("  Hello    world   ")
        self.assertEqual(processor.raw_text, "Hello world")

    def test_parse_text_with_punctuation(self):
        processor = TextProcessor("Hello world. Test case!")
        self.assertEqual(len(processor.text.sentences), 2)

    def test_parse_text_without_punctuation(self):
        
        processor = TextProcessor("Hello world")
        self.assertGreaterEqual(len(processor.text.sentences), 0)

    def test_get_all_words(self):
        processor = TextProcessor("Hello world. Test case.")
        words = processor.get_all_words()

        self.assertEqual(len(words), 4)
        self.assertEqual(str(words[0]), "Hello")

    def test_sorting_logic(self):
        processor = TextProcessor("aaa bb cccc")
        words = processor.get_all_words()

        sorted_words = sorted(words, key=lambda w: (w.length(), -w.vowel_count()))

        self.assertEqual(str(sorted_words[0]), "bb")
        self.assertEqual(str(sorted_words[-1]), "cccc")

    def test_search_word(self):
        processor = TextProcessor("Gandalf is here.")
        words = processor.get_all_words()

        target = Word([Letter(c) for c in "Gandalf"])
        found = any(w == target for w in words)

        self.assertTrue(found)


if __name__ == "__main__":
    unittest.main()
