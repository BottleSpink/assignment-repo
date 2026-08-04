"""
Exercise 3 — N-grams

Implement the 5 functions below. They ramp from easy to make-you-think.
Pure Python — no imports needed. Don't rename functions or change arguments.

Test locally:  python selfcheck.py   (run from inside the ex3 folder)
Then commit & push this file. Your score updates on the leaderboard.
"""


def unigrams(tokens):
    """Q1. Return the list of unigrams: just each token as a
    1-tuple, in order.
    Example: unigrams(["the","cat"]) -> [("the",), ("cat",)]
    """
    # your code here
    pass


def bigrams(tokens):
    """Q2. Return the list of consecutive bigrams as 2-tuples.
    If fewer than 2 tokens, return [].
    Example: bigrams(["the","cat","sat"])
             -> [("the","cat"), ("cat","sat")]
    """
    # your code here
    pass


def ngrams(tokens, n):
    """Q3. Return the list of n-grams as n-tuples, in order.
    If n > len(tokens) or n <= 0, return [].
    Example: ngrams(["a","b","c","d"], 3)
             -> [("a","b","c"), ("b","c","d")]
    Example: ngrams(["a","b"], 5) -> []
    """
    # your code here
    pass


def count_bigrams(tokens):
    """Q4. Return a dict mapping each bigram (2-tuple) to how many
    times it occurs.
    Example: count_bigrams(["a","b","a","b"])
             -> {("a","b"): 2, ("b","a"): 1}
    """
    # your code here
    pass


def most_common_bigram(tokens):
    """Q5. Return the single most frequent bigram (2-tuple).
    On a TIE, return the bigram that appears FIRST in `tokens`.
    If there are no bigrams, return None.
    Example: most_common_bigram(["a","b","a","b","c"])
             -> ("a","b")
    Example: most_common_bigram(["x","y","y","x"])   # all count 1, tie
             -> ("x","y")   (appears first)
    """
    # your code here
    pass
