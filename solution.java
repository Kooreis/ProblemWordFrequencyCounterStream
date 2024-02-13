Here is a simple Java console application that implements a word frequency counter using a stream of words:

```java
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a sentence:");
        String sentence = scanner.nextLine();
        String[] words = sentence.split("\\s+");
        Map<String, Long> wordCount = new HashMap<>();

        Arrays.stream(words).forEach(word -> {
            word = word.toLowerCase();
            if (wordCount.containsKey(word)) {
                wordCount.put(word, wordCount.get(word) + 1);
            } else {
                wordCount.put(word, 1L);
            }
        });

        System.out.println("Word Frequencies:");
        wordCount.forEach((word, count) -> System.out.println(word + ": " + count));
    }
}
```

This program reads a sentence from the console, splits it into words, and then uses a stream to process each word. For each word, it checks if the word is already in the map. If it is, it increments the count. If it's not, it adds the word to the map with a count of 1. Finally, it prints out the frequencies of each word.