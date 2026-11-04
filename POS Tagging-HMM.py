tags = ["D", "N", "V"]
emission = {
"the": {"D": 0.9},
"a": {"D": 0.9},
"dog": {"N": 0.8},
"cat": {"N": 0.8},
"barks": {"V": 0.8},
"sleeps": {"V": 0.8}
}
sentence = "the dog barks".split()
tagged = []
for word in sentence:
scores = {tag: emission.get(word, {}).get(tag, 0.01) for tag in tags}
tagged.append((word, max(scores, key=scores.get)))
print("Tagged sentence:")
for word, tag in tagged:
print(word, "/", tag)
