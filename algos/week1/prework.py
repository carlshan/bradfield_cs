#!#/usr/bin/python3

"""
Prework for Week 1 (March 30) included the following:

1. Reading a summary of George Polya's How to Solve It: https://math.berkeley.edu/~gmelvin/polya.pdf
2. Completing the following exercise:

> Apangram is a phrase which contains every letter at least once, such as “the quick brown fox jumps over the lazy dog”. 
> Write a function which determines if a given string is a pangram.
> This should be an easy problem, so it’s a good excuse to practice Polya’s methoxwd. 
> So, please find at least three different strategies for solving this problem, proceeding through Polya’s method each time. 
> In each case, make a note of how you came to that. Please submit your solutions by Slack to your instructor prior to the start of class.

""" 

# Approach No. 1 -- Naive, simple approach of checking each letter

alphabet = list('abcdefghijklmnopqrstuvwxyz')
test_string_pass = "the quick brown fox jumps over the lazy dog"
test_string_fail = "the quick brown fox jumps over the lazy do"

def is_pangram_1(string, alphabet):
    """
        Uses the `in` infix operator to scan if each letter is in the string.
    """
    string = string.lower()

    for letter in alphabet: 
        if letter not in string: # downside: has to scan the whole string len(alphabet) times
            return False

    return True


print(is_pangram_1(test_string_pass, alphabet))
print(is_pangram_1(test_string_fail, alphabet))

# Approach No. 2 -- Comparing sets

def is_pangram_2(string, alphabet):
    """
        A string that has all of the letters in a given alphabet must satisfy the following:
            * The intersection of string and alphabet must be the complete alphabet
    """
    string = string.lower()

    unique_letters = set(string) # scans string once to get unique elements (I assum it only scans the string once)

    return len(unique_letters.intersection(alphabet)) == len(alphabet) # scans alphabet once

print(is_pangram_2(test_string_pass, alphabet))
print(is_pangram_2(test_string_fail, alphabet))

# Approach No. 3 -- Improving upon approach number 1
def is_pangram_3(string, alphabet):
    """
        Improves upon is_pangram_1 by reducing the length of the string that needs to be scanned over
    """
    string = string.lower()

    to_scan = string
    for letter in alphabet:
        if letter not in to_scan:
            return False
        else:
            to_scan = to_scan.replace(letter, '') # shortening the string to be scanned each time by stripping out all of the extraneous letters we no longer need to check for
            # although I suppose .replace has to scan to_scan each time as well. If there are a lot of duplications in the string, this can speed things up, else this adds extra overhead.
    
    return True

print(is_pangram_3(test_string_pass, alphabet))
print(is_pangram_3(test_string_fail, alphabet))


# Approach No 4. Only iterate through the string once. I implemented this myself after seeing Elliot's video on it.
def is_pangram_4(string, alphabet):
    string = string.lower()

    seen_letters = set()
    for char in string:
        seen_letters.add(char)

    for letter in alphabet:
        if letter not in seen_letters:
            return False
    
    return True


print(is_pangram_4(test_string_pass, alphabet))
print(is_pangram_4(test_string_fail, alphabet))


"""
The solutions provided by Bradfield contained the following bitwise example:

def is_pangram_bitset(phrase):
    s = 0
    for c in phrase:
        if c.isalpha():
            s |= ( 1 << (ord(c) - ord('a')) )
    return s == 0x3ffffff


How does it work?

First off, what does the line `s |= (1 << (ord(c) - ord('a')))` do?

x << y returns x with bits shifted to the left by y places, equivalent to multiplying x by 2**y

So in this case, 1 is being multiplied by 2**(ord(c) - ord('a'))

ord('c') - ord('a') essentially returns the index position of the letter c in an ordered alphabet (i.e. 'a' is index 0 in 'abcd...xyz')

So the expression 1 << ord('c') - ord('a') resolves into:

If char='a' -> 0 -> (ord('a') - ord('a')) -> 1 * 2**0 = 1
If char='b' -> 1 -> 1 * 2**1 = 2
If char='c' -> 2 -> 1 * 2**2 = 4

... and so on. Essentially creating all the powers of 2 up to 2**25, which in binary is simply the number 1 in the place of the xth power of 2 and 0 elsewhere. Since the powers of two are used in binary representation,
1 << (ord(c) - ord('a')) is a quick way to create the binary representation of the variable c .

s |= will reassign s to be the value of a bitwise `or` between the previous s and the current power of 2. This "fills up" the binary representation of the value 's' with 1's wherever a letter has been seen.

So s essentially builds up the binary representation of 2^25.

At the very end we check if s == 0x3ffffff, as 0x3ffffff is essentially the number that is represented in binary as '11111111111111111111111111' (26 1's). If s == 0x3ffffff, then this would imply every letter has been seen.

"""

def is_pangram_bitset(phrase):
    phrase = phrase.lower()

    s = 0
    for c in phrase:
        if c.isalpha():
            s |= ( 1 << (ord(c) - ord('a')) )
    return s == 0x3ffffff

print(is_pangram_bitset(test_string_pass))
print(is_pangram_bitset(test_string_fail))