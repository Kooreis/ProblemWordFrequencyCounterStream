class WordFrequencyCounter:
    def __init__(self):
        self.word_frequencies = {}

    def add_word(self, word):
        if word in self.word_frequencies:
            self.word_frequencies[word] += 1
        else:
            self.word_frequencies[word] = 1