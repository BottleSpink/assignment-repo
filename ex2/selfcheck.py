"""Local sample check for ex2."""
import solution as s
samples = [
    ("get_suffix", ("running",3), "ing"),
    ("is_plural", ("cats",), True),
    ("stem", ("played",), "play"),
    ("pluralize", ("baby",), "babies"),
    ("count_morphemes", ("playings",["s","ing"]), 3),
]
p=0
for fn,args,exp in samples:
    try: got=getattr(s,fn)(*args)
    except Exception as e: print(f"FAIL {fn}: raised {type(e).__name__}: {e}"); continue
    if got==exp: print(f"PASS {fn}"); p+=1
    else: print(f"FAIL {fn}: expected {exp!r}, got {got!r}")
print(f"\n{p}/{len(samples)} sample cases passed.")
