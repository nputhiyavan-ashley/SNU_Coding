import java.util.*;
import java.io.*;

class WordCount {
    String[] Split(String input) {
        String[] parts = input.split(" ");
        return parts;
    }

    String[] remove_punctuation(String[] input) {
        String[] output = new String[input.length];
        for (int i = 0; i < input.length; i++) {
            output[i] = input[i].replaceAll("[^a-zA-Z]", "").toLowerCase();
        }
        return output;
    }

    String[][] Count(String[] input) {
        HashMap<String, Integer> wordCount = new HashMap<>();

        for (String word : input) {
            wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);
        }

        String[][] output = new String[wordCount.size()][2];
        int index = 0;
        for (Map.Entry<String, Integer> entry : wordCount.entrySet()) {
            output[index][0] = entry.getKey();
            output[index][1] = String.valueOf(entry.getValue());
            index++;
        }

        return output;
    }

    
    String[][] Sort_count(String[][] input) {
        Arrays.sort(input, (a, b) -> Integer.compare(Integer.parseInt(b[1]), Integer.parseInt(a[1])));
        return input;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String input = sc.nextLine();

        WordCount obj = new WordCount();

        String[] splited_input = obj.Split(input);
        String[] cleaned_input = obj.remove_punctuation(splited_input);
        String[][] word_count = obj.Count(cleaned_input);
        String[][] sorted_word_count = obj.Sort_count(word_count);

        for(int  i=0; i<3; i++) {
            System.out.println(sorted_word_count[i][0] + " : " + sorted_word_count[i][1]);
        }

    }
}

//Sample Input: "Hello world! This is a test. Hello again, world."
//Sample Output:
//Top 3 frequentwords: 
//hello : 2
//world : 2
//this : 1

