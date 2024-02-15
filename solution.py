class WordFrequencyCounter:
    ...

    def get_frequency(self, word):
        if word in self.word_frequencies:
            return self.word_frequencies[word]
        else:
            return 0