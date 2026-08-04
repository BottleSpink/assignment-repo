"""
Exercise 1 — Regular Expressions

Implement the 5 functions below. They ramp from easy to make-you-think.
Use the `re` module. Don't rename functions or change arguments.

Test locally:  python selfcheck.py   (run from inside the ex1 folder)
Then commit & push this file. Your score updates on the leaderboard.

Points: Q1=10, Q2=15, Q3=20, Q4=25, Q5=30  (total 100)
"""
import re


def find_words(text):
    """Q1 (10 pts). Return a list of all word tokens in `text`.
    A "word" is one or more word-characters (letters, digits, underscore).
    Order = left to right as they appear.
    Example: find_words("Hi there, cats!") -> ['Hi', 'there', 'cats']
    """
    # your code here
    pass


def extract_numbers(text):
    """Q2 (15 pts). Return a list of all numbers (as strings) in `text`.
    A number is one or more digits, optionally followed by a decimal point
    and more digits. Integers and decimals both count.
    Example: extract_numbers("I paid 3.50 for 2 cats in 2024")
             -> ['3.50', '2', '2024']
    """
    # your code here
    pass


def find_capitalized(text):
    """Q3 (20 pts). Return a list of words that START with an uppercase letter.
    A word starts at a word boundary. Keep original casing. Left to right.
    Example: find_capitalized("The striped Cat met Alice")
             -> ['The', 'Cat', 'Alice']
    """
    # your code here
    pass


def find_repeated_words(text):
    """Q4 (25 pts). Return a list of words that appear TWICE IN A ROW
    (a doubled word), matched CASE-INSENSITIVELY. Return each repeated word
    LOWERCASED, in the order the repeats occur.
    A repeat = the same word, separated only by whitespace.
    Example: find_repeated_words("the the cat sat sat down")
             -> ['the', 'sat']
    Example: find_repeated_words("The the dog")   # case-insensitive
             -> ['the']
    Hint: back-references. (\\w+)\\s+\\1  ... and think about the flag.
    """
    # your code here
    pass


def mask_phone(text):
    """Q5 (30 pts). Replace every phone number with the literal <PHONE>.
    A phone number here is exactly: 3 digits, a hyphen, 4 digits  (555-1234).
    Return the resulting string. Everything else stays unchanged.
    Example: mask_phone("Call 555-1234 or 555-5678 now")
             -> "Call <PHONE> or <PHONE> now"
    """
    # your code here
    pass
