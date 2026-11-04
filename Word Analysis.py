word = input("Enter a word: ").strip()
prefixes = ["un", "re", "dis", "pre", "mis"]
suffixes = ["ing", "ed", "ly", "s", "er", "ness"]
w = word.lower()
prefix = next((p for p in prefixes if w.startswith(p) and len(w) > len(p)), "")
suffix = next((s for s in suffixes if w.endswith(s) and len(w) > len(s)), "")
stem = w
if prefix:
stem = stem[len(prefix):]
if suffix and stem.endswith(suffix):
stem = stem[:-len(suffix)]
print("Word:", word)
print("Length:", len(word))
print("Prefix:", prefix if prefix else "None")
print("Suffix:", suffix if suffix else "None")
print("Possible stem:", stem)
