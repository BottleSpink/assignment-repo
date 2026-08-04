"""Local sample check for ex3"""
import solution as s
samples = [
    ("unigrams", (["the","cat"],), [("the",),("cat",)]),
    ("bigrams", (["the","cat","sat"],), [("the","cat"),("cat","sat")]),
    ("ngrams", (["a","b","c","d"],3), [("a","b","c"),("b","c","d")]),
    ("count_bigrams", (["a","b","a","b"],), {("a","b"):2,("b","a"):1}),
    ("most_common_bigram", (["a","b","a","b","c"],), ("a","b")),
]
p=0
for fn,args,exp in samples:
    try: got=getattr(s,fn)(*args)
    except Exception as e: print(f"FAIL {fn}: raised {type(e).__name__}: {e}"); continue
    if got==exp: print(f"PASS {fn}"); p+=1
    else: print(f"FAIL {fn}: expected {exp!r}, got {got!r}")
print(f"\n{p}/{len(samples)} sample cases passed.")
