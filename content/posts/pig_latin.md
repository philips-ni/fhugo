+++
title = "pig_latin"
author = ["Fei Ni"]
date = 2021-05-03T06:49:00-07:00
lastmod = 2021-05-03T06:49:00-07:00
tags = ["helix", "interview"]
categories = ["helix"]
draft = false
+++

## <span class="section-num">1</span> Description {#description}

-   General rule: take the first letter of a word, move it to the end, and add "ay". Example: "hello" becomes "ellohay".
-   A phrase with multiple words should translate each word: "hello world" becomes "ellohay orldway"
-   A word which begins with a vowel keeps its first letter, and just adds "way" to the end of the word: "eat apples" becomes "eatway applesway"
-   A word which is capitalized should remain capitalized after translation: "Hello world" becomes "Ellohay orldway"
-   A phrase with punctuation should maintain the position of the punctuation: "Hello, world!" becomes "Ellohay, orldway!"
-   A word beginning with multiple consonants should move all of them together to the end: "drunk strangers" becomes "unkdray angersstray"
-   The letters "qu" should stay together when moved to the end of a word: "quickly and quietly" becomes "icklyquay andway ietlyquay"


## <span class="section-num">2</span> Solutions {#solutions}


### <span class="section-num">2.1</span> Python solutions {#python-solutions}

```python
def convertWord(s):
    if s == "":
        return s
    # rule 5
    if s[-1] in ['!', ",", "."]:
       return convertWordCore(s[:-1]) + s[-1]
    else:
       return convertWordCore(s)

def getVowelIndex(s):
    for i,val in enumerate(s):
        # rule 7, if "u" is part of "qu" don't treat it as vowel
        if val in "aeiouAEIOU" and (i > 0 and s[i-1:i+1] != "qu"):
            return i
    return -1

def convertWordCore(s):
    # rule 2
    if s[0] in "aeiouAEIOU":
        ret = s + "way"
    else:
        vowelIndex = getVowelIndex(s)
        if vowelIndex == -1:
            ret = s + "ay"
        else:
            # rule 4 and 1
            if s[0].isupper():
                # rule 6
                ret = s[vowelIndex:].capitalize() + s[:vowelIndex].lower() + "ay"
            else:
                ret = s[vowelIndex:] + s[:vowelIndex] + "ay"
    return ret


def convertSentence(s):
    words = []
    word = ""
    convertedWords = []
    for c in s:
        if c in [",", "!"]:
            words.append(word + c)
            word = ""
        elif c == " ":
            words.append(word)
            word = ""
        else:
            word += c
    if word != "":
        words.append(word)
    # rule 2
    for word in words:
        convertedWords.append(convertWord(word))
    return " ".join(convertedWords)

inputs = ["Hello world", "Hello,world!", "eat apples", "bybye", "quickly and quietly", "ququi"]
for input in inputs:
    print("{} -> {}".format(input, convertSentence(input)))


```


### <span class="section-num">2.2</span> Java Solutions {#java-solutions}

```java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
// 1. General rule: take the first letter of a word, move it to the end, and add "ay". Example: "hello" becomes "ellohay".
// 2. A phrase with multiple words should translate each word: "hello world" becomes "ellohay orldway"
// 3. A word which begins with a vowel keeps its first letter, and just adds "way" to the end of the word: "eat apples" becomes "eatway applesway"
// 4. A word which is capitalized should remain capitalized after translation: "Hello world" becomes "Ellohay orldway"
// 5. A phrase with punctuation should maintain the position of the punctuation: "Hello, world!" becomes "Ellohay, orldway!"
public class Solution {
    public static void main(String args[] ) throws Exception {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT */
        String s = "hello this is an example";
        String s2 = "hello world";
        String s3 = "eat apples";
        String s4 = "Hello world";
        String[] words = new String[]{s, s2, s3, s4,
            "", "   ", "HELLO WORLD", //"hello   worlds  ",// "Hello, world!",
        };
        for (String word : words) {
            String newWord = convertString(word);
            System.out.printf("OUTPUT: %s -> %s\n", word, newWord);
        }
    }
    public static final HashSet<Character> VOWELS = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));
    public static String convertWord(String word) {
        if (word.length() == 0) return "";
        char c = word.charAt(0);
        if (VOWELS.contains(c)) {
            return word + "way";
        } else {
            boolean isCapitalized = c >= 'A' && c <= 'Z';
            // make c lower
            if (isCapitalized) {
                c = Character.toLowerCase(c);
            }
            // take care of first char in new word
            String newWord = word.substring(1) + c + "ay";
            if (!isCapitalized) return newWord;
            c = newWord.charAt(0);
            c = Character.toUpperCase(c);
            return "" + c + newWord.substring(1);
        }
    }
    // public static String convertWord(String word) {
    //     if (word.length() == 0) return "";
    //     char c = word.charAt(0);
    //     if (VOWELS.contains(c)) {
    //         return word + "way";
    //     } else {
    //         return word.substring(1) + c + "ay";
    //     }
    // }
    // public static String convertWord(String word) {
    //     if (word.length() == 0) return "";
    //     return word.substring(1) + word.charAt(0) + "ay";
    // }
    public static String convertString(String s) {
        if (s.length() == 0) return s;
        String[] words = s.split("\\s+");
        StringBuilder sb = new StringBuilder();
        for (String word : words) {
            sb.append(convertWord(word)).append(" ");
        }
        if (sb.length() > 0) {
            sb.setLength(sb.length() - 1);
        }
        return sb.toString();
    }
}
```


### <span class="section-num">2.3</span> Golang Solutions {#golang-solutions}

see [here](https://play.golang.org/p/Pb0t927buwM)


## <span class="section-num">3</span> Links {#links}

-   <https://github.com/myhelix/eng%5Finterviews/>
-   <https://myhelix.atlassian.net/wiki/spaces/ENG/pages/51350447/Interviewing+Engineers>
