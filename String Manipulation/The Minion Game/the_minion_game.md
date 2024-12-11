The Minion game involves two players (Kevin and Stuart) who score points by creating substrings from a given string.
Kevin scores for substrings starting with vowels, and Stuart scores for substrings starting with consonants. The player with the highest score wins the game.

## Problem Overview
The game works as follows:

* You are given a string `S` of length `n`.
* Kevin scores points for all substrings starting with a vowel (A, E, I, O, U).
* Stuart scores points for all substrings starting with a consonant.
* The score for a substring starting at position `i` is `(n - i)` because all substrings starting from `i` contribute `(n - i)` points.
* The game ends when all possible substrings are considered, and the player with the highest score wins.

**Input**: You input a string consisting of uppercase English letters.<br>
```
BANANA
```

**Output**: The program will output the winner (either "Kevin" or "Stuart") and their score. If it's a tie, it will print "Draw".
```
Stuart 12
```

<a href="https://medium.com/@s.stuti990/the-minion-game-hackerrank-4f16d5505541" target="_blank">Click here</a> for the explanation of this coding challenge.
