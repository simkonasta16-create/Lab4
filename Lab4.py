import re

class Letter:
    def __init__(self, char: str):
        self.char = char

    def __repr__(self):
        return self.char


class Word:
    def __init__(self, letters):
        self.letters = letters

    def __repr__(self):
        return "".join(str(l) for l in self.letters)

    def __eq__(self, other):
        if not isinstance(other, Word):
            return False
        return str(self) == str(other)

    def length(self):
        return len(self.letters)

    def vowel_count(self):
        vowels = "aeiouаеєиіїоуюяAEIOUАЕЄИІЇОУЮЯ"
        return sum(1 for l in self.letters if l.char in vowels)


class Punctuation:
    def __init__(self, symbol: str):
        self.symbol = symbol

    def __repr__(self):
        return self.symbol


class Sentence:
    def __init__(self, elements):
        self.elements = elements

    def __repr__(self):
        result = ""
        for e in self.elements:
            if isinstance(e, Punctuation):
                result += str(e)
            else:
                if result:
                    result += " "
                result += str(e)
        return result


class Text:
    def __init__(self, sentences):
        self.sentences = sentences

    def __repr__(self):
        return "\n".join(str(s) for s in self.sentences)


class TextProcessor:
    def __init__(self, raw_text: str):
        self.raw_text = self.clean_text(raw_text)
        self.text = self.parse_text(self.raw_text)

    def clean_text(self, text):
        return re.sub(r'\s+', ' ', text).strip()

    def parse_text(self, text):
        sentences_raw = re.split(r'([.!?])', text)
        sentences = []

        for i in range(0, len(sentences_raw), 2):
            sentence_text = sentences_raw[i].strip()
            if not sentence_text:
                continue

            punctuation = sentences_raw[i + 1] if i + 1 < len(sentences_raw) else ""

            words = []
            for word in sentence_text.split():
                letters = [Letter(ch) for ch in word]
                words.append(Word(letters))

            elements = words
            if punctuation:
                elements.append(Punctuation(punctuation))

            sentences.append(Sentence(elements))

        return Text(sentences)

    def get_all_words(self):
        words = []
        for sentence in self.text.sentences:
            for el in sentence.elements:
                if isinstance(el, Word):
                    words.append(el)
        return words

    def process(self):
        words = self.get_all_words()

        print("Початкові слова:")
        for w in words:
            print(f"{w} | len:{w.length()} | vowels:{w.vowel_count()}")

        sorted_words = sorted(words, key=lambda w: (w.length(), -w.vowel_count()))

        print("\nВідсортовані слова (len ↑, vowels ↓):")
        for w in sorted_words:
            print(f"{w} | len:{w.length()} | vowels:{w.vowel_count()}")

        target = Word([Letter(ch) for ch in "Gandalf"])

        found = False
        for w in sorted_words:
            if w == target:
                print("\nЗнайдено слово:")
                print(w)
                found = True
                break

        if not found:
            print("\nСлово не знайдено")


def main():
    text = "   Aragorn is a king.  Gandalf is a mage.   Legolas is a prince   "

    processor = TextProcessor(text)

    print("Текст після обробки:\n")
    print(processor.text)

    print("\n--- Обробка ---\n")
    processor.process()


if __name__ == "__main__":
    main()