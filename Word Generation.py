def pluralize(word):
w = word.lower()
irregular = {"child": "children", "man": "men", "woman": "women",
"person": "people", "mouse": "mice"}
if w in irregular:
return irregular[w]
if w.endswith("y") and len(w) > 1 and w[-2] not in "aeiou":
return w[:-1] + "ies"
if w.endswith(("s", "x", "z", "ch", "sh")):
return w + "es"
if w.endswith("fe"):
return w[:-2] + "ves"
if w.endswith("f"):
return w[:-1] + "ves"
return w + "s"
words = ["city", "child", "boy", "bus", "knife"]
for word in words:
print(word, "->", pluralize(word))
