Here is a simple console application in C# that implements a word frequency counter using a stream of words:

```C#
using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Enter a stream of words:");
        string input = Console.ReadLine();
        CountWordFrequency(input);
    }

    static void CountWordFrequency(string input)
    {
        Dictionary<string, int> wordFrequency = new Dictionary<string, int>();

        string[] words = input.Split(' ');

        foreach (string word in words)
        {
            if (wordFrequency.ContainsKey(word))
            {
                wordFrequency[word]++;
            }
            else
            {
                wordFrequency[word] = 1;
            }
        }

        foreach (KeyValuePair<string, int> entry in wordFrequency)
        {
            Console.WriteLine("Word: {0}, Frequency: {1}", entry.Key, entry.Value);
        }
    }
}
```

This program reads a line of text from the console, splits it into words, and counts the frequency of each word using a dictionary. The frequency of each word is then printed to the console.