# Question: How do you implement a word frequency counter using a stream of words? C# Summary

The C# console application is designed to count the frequency of words in a given stream of words. The program begins by prompting the user to enter a stream of words. The entered string is then passed to the CountWordFrequency method. This method initializes a dictionary to store each unique word and its corresponding frequency. The input string is split into individual words based on spaces. The program then iterates over each word. If the word is already present in the dictionary, its frequency count is incremented by one. If the word is not present, it is added to the dictionary with a frequency count of one. After all words have been processed, the program iterates over the dictionary and prints each word along with its frequency to the console. This way, the program effectively counts the frequency of each word in the input stream.

---

# Python Differences

The Python version of the solution is more interactive than the C# version. It continuously takes input from the user until the user decides to quit. The user can add words to the counter one by one and can also check the frequency of a specific word at any time. This is different from the C# version where the user enters a stream of words at once and the program counts the frequency of each word in the stream and then ends.

In terms of language features, both versions use a dictionary (or a similar data structure) to store the word frequencies. The Python version uses a class to encapsulate the word frequency counter, while the C# version uses a static method in the main program class. 

The Python version uses the `input()` function to get user input, while the C# version uses `Console.ReadLine()`. The Python version uses the `in` keyword to check if a word is in the dictionary, while the C# version uses the `ContainsKey()` method. 

The Python version uses a `while True` loop to continuously take user input, and breaks the loop when the user enters 'quit'. The C# version does not have a similar loop, it only takes user input once.

The Python version also has a `get_frequency()` method that returns the frequency of a specific word, which the C# version does not have. Instead, the C# version prints the frequency of all words after counting them.

---

# Java Differences

Both the C# and Java versions solve the problem in a similar way. They both read input from the console, split the input into words, and then count the frequency of each word using a dictionary (in C#) or a map (in Java). The frequency of each word is then printed to the console.

However, there are a few differences in the language features and methods used:

1. Input Reading: In C#, the `Console.ReadLine()` method is used to read the input. In Java, a `Scanner` object is used to read the input.

2. Word Splitting: Both versions split the input into words using the `split` method. However, the Java version uses a regular expression (`\\s+`) to split the input on one or more whitespace characters, while the C# version simply splits on a single space character (' ').

3. Word Counting: Both versions use a dictionary/map to count the word frequencies. However, the Java version uses a `HashMap` and the C# version uses a `Dictionary`. The Java version also converts each word to lower case before counting it, which the C# version does not do.

4. Stream Processing: The Java version uses a stream (`Arrays.stream(words)`) to process each word. This allows it to use the `forEach` method to apply a lambda function to each word. The C# version uses a `foreach` loop to iterate over the words.

5. Output: Both versions print the word frequencies to the console. However, the Java version uses a lambda function with the `forEach` method to print each word and its frequency, while the C# version uses a `foreach` loop and the `Console.WriteLine` method.

---
