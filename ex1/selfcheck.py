"""Local sample check for ex1. A few cases so you can test before pushing.
NOT the full hidden suite — passing these doesn't guarantee full marks."""
import solution as s
samples = [
    ("find_words", ("Hi there, cats!",), ['Hi','there','cats']),
    ("extract_numbers", ("I paid 3.50 for 2 cats in 2024",), ['3.50','2','2024']),
    ("find_capitalized", ("The striped Cat met Alice",), ['The','Cat','Alice']),
    ("find_repeated_words", ("the the cat sat sat down",), ['the','sat']),
    ("mask_phone", ("Call 555-1234 now",), "Call <PHONE> now"),
]
p=0
for fn,args,exp in samples:
    try: got=getattr(s,fn)(*args)
    except Exception as e: print(f"FAIL {fn}: raised {type(e).__name__}: {e}"); continue
    if got==exp: print(f"PASS {fn}"); p+=1
    else: print(f"FAIL {fn}: expected {exp!r}, got {got!r}")
print(f"\n{p}/{len(samples)} sample cases passed.")
