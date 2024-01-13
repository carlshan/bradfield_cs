# Interview Practice Questions

Compiled by Carl Shan.

## General Programming Interview Advice

1. **Listen**: Listen carefully to the problem and repeat the crux of the question back afterwards to ensure complete understanding.
2. **Offer Examples**: examples of what output a successful program should return, and also offer examples of a failed case, as well as edge cases.
3. **Problem Solve without Code**: Sketch out a rough solution by hand, verbally explaining your reasoning and assumptions so that the interviewer could correct you.
4. **Implement in Code**: Write code, explaining how you are translating your solution into code as you go along.
5. **Ask for Feedback**: Ask for feedback and suggestions for improvement.

## String Manipulation

1. Write a program that returns whether a string is a pangram. A pangram is a string that contains all 26 letters of the alphabet.
2. Write a program that returns whether a string is a palindrome.
3. Write a program that finds the longest palindrome in a string.
4. Write a function that returns a list of all the duplicate characters in a string.
5. Check if a string is an anagram of another string.
6. Write a function that will return if a string is a rotation of another given string.
7. Count occurrences of a word in a given string.

## Other Questions (with an emphasis on data structures and algorithms)

1. Implement at least 3 different ways of finding the factorial of a number.
2. Count the number of ways that someone can fill a rectangular tile that is 1xN with some combination of `1x1` blue and `1x2` red pieces. A combination is considered unique if it looks unique.
3. Check to see if an equation has balanced parentheses.
4. Given a string that contains a filepath, with special characters `'.'` (meaning the current directory) and `'..'` (meaning the parent directory), implement a function that resolves this string to the appropriate filepath without the `'.'` and `'..'` characters.
5. Given two jugs that can contain water up to limits `A` and `B` respectively (e.g., 3 and 5), return the number of steps involved in order to have one of the jugs contain `target` units of water.
6. Implement Breadth-First Search, Depth-First Search or Dijkstra's algorithm over a provided graph. What data structures did you choose and why?
7. Implement Binary Search recursively with and without indices over an array.
8. Count the number of inversions in a list of numbers.
9. Solve [Frog 1](https://atcoder.jp/contests/dp/tasks/dp_a).
   *  **Advanced**: Now solve [Frog 2](https://atcoder.jp/contests/dp/tasks/dp_b).
10. Given a knapsack with a specific carrying capacity `W`, determine the maximum value of items contained in the set `[ { "weight": 5, "value": 10 }, { "weight": 4, "value": 40 }, { "weight": 6, "value": 30 }, { "weight": 4, "value": 50 } ]` or any arbitrary set. (From Exercism).
11. Given an alphabet, return all `2` letter combinations of this alphabet. Now generalize to `N` letter combinations.
12. Given a lattice of height `h` and width `w`, how many unique shortest paths exist from the top left corner to the bottom right corner? For example, given a lattice with dimensions `h=w=2`, there are `6` unique paths.

## Other problems (with a focus on building complex software)

1. Implement a simple interactive version of Tic-Tac-Toe
2. Implement rock-paper-scissors. Now implement an AI that plays RPS better than chance.
3. Implement a two-player game of [Nim](https://iq.opengenus.org/game-of-nim/). Now implement a program that can be played against. Can you improve this program so that it does better than randomly taking remaining items?

## Other Interviewing Resources:

1. Cracking the Coding Interview by Gayle McDowell
2. [Interactive Coding Exercises (with Flashcards)](https://github.com/donnemartin/interactive-coding-challenges) by Donne Martin
3. [Anonymous interviews online](https://interviewing.io/) and live [YouTube videos](https://www.youtube.com/channel/UCNc-Wa_ZNBAGzFkYbAHw9eg).
4. [How to pass a programming interview](https://triplebyte.com/blog/how-to-pass-a-programming-interview) by TripleByte.