def analyze_morphology(word):
suffixes = ["ing", "ed", "es", "s", "er", "est", "ly", "ness"]
w = word.lower()
for suffix in sorted(suffixes, key=len, reverse=True):
if w.endswith(suffix) and len(w) > len(suffix):
return w[:-len(suffix)], suffix
return w, ""
words = ["playing", "walked", "cats", "kindness", "book"]
for word in words:
stem, suffix = analyze_morphology(word)
print(f"{word}: stem={stem}, suffix={suffix or 'None'}")
