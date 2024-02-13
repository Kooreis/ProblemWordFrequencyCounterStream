Here is a Python console application that implements a word frequency counter using a stream of words:

```python
class WordFrequencyCounter:
    def __init__(self):
        self.word_frequencies = {}

    def add_word(self, word):
        if word in self.word_frequencies:
            self.word_frequencies[word] += 1
        else:
            self.word_frequencies[word] = 1

    def get_frequency(self, word):
        if word in self.word_frequencies:
            return self.word_frequencies[word]
        else:
            return 0

def main():
    counter = WordFrequencyCounter()
    while True:
        print("Enter a word to add to the counter, or 'get' to get the frequency of a word, or 'quit' to quit.")
        command = input()
        if command == 'quit':
            break
        elif command == 'get':
            print("Enter the word you want to get the frequency of.")
            word = input()
            print("The frequency of", word, "is", counter.get_frequency(word))
        else:
            counter.add_word(command)

if __name__ == "__main__":
    main()
```

This application continuously takes input from the user. If the user enters 'get', the application will ask for a word and then print the frequency of that word. If the user enters 'quit', the application will stop. Otherwise, the application will add the entered word to the counter.