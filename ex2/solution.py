"""
Exercise 2 — Morphology

Implement the 5 functions below. They ramp from easy to make-you-think.
Pure Python — no imports needed. Don't rename functions or change arguments.

Test locally:  python selfcheck.py   (run from inside the ex2 folder)
Then commit & push this file. Your score updates on the leaderboard.

"""


def get_suffix(word, k):
    """Q1. Return the last `k` characters of `word`.
    If k >= len(word), return the whole word. If k <= 0, return "".
    Example: get_suffix("running", 3) -> "ing"
    """
    # your code here
    pass


def is_plural(word):
    """Q2. Return True if `word` looks like a regular plural, else False.
    Rule: ends in 's' BUT NOT in 'ss'.
    Examples: is_plural("cats") -> True, is_plural("class") -> False,
              is_plural("cat") -> False
    """
    # your code here
    pass


def stem(word):
    """Q3. Strip ONE suffix using this EXACT ordered rule set.
    Check suffixes in THIS ORDER; strip the FIRST that matches AND that
    leaves a stem of length >= 2. If none match, return the word unchanged.
    Order: "ing", "ed", "ly", "es", "s"
    Examples: stem("running") -> "runn"   (strip "ing")
              stem("played")  -> "play"   (strip "ed")
              stem("cats")    -> "cat"    (strip "s")
              stem("is")      -> "is"     (stripping "s" would leave "i", len<2)
    """
    # your code here
    pass


def pluralize(word):
    """Q4. Return the plural of `word` using THESE EXACT rules,
    checked in order:
      1. ends in 's','x','z','ch','sh'      -> add "es"   (box->boxes, bus->buses)
      2. ends in consonant + 'y'            -> replace 'y' with "ies" (baby->babies)
         (a 'y' preceded by a vowel a/e/i/o/u does NOT change: boy->boys)
      3. otherwise                          -> add "s"    (cat->cats)
    Assume lowercase input.
    Examples: pluralize("box")->"boxes", pluralize("baby")->"babies",
              pluralize("boy")->"boys", pluralize("cat")->"cats",
              pluralize("church")->"churches"
    """
    # your code here
    pass


def count_morphemes(word, affixes):
    """Q5. Count morphemes = 1 (the stem) + number of affixes present.
    `affixes` is a list of suffix strings. Strip affixes GREEDILY and REPEATEDLY
    from the END: each time the current word ends with any affix in the list
    (check the list in order, take the first match) AND stripping leaves length
    >= 2, strip it and count +1. Stop when no affix matches.
    Return the total morpheme count (stem counts as 1, even if 0 affixes found).
    Example: affixes=["s","ing"]
      count_morphemes("plays", ["s","ing"]) -> 2   (play + s)
      count_morphemes("playings", ["s","ing"]) -> 3 (play + ing + s)
      count_morphemes("cat", ["s","ing"]) -> 1     (just the stem)
    """
    # your code here
    pass
