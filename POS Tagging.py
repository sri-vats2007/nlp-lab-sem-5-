from collections import defaultdict, Counter
training = [
[("the", "DET"), ("dog", "NOUN"), ("runs", "VERB")],
[("a", "DET"), ("cat", "NOUN"), ("sleeps", "VERB")],
[("the", "DET"), ("cat", "NOUN"), ("runs", "VERB")]
]
word_tags = defaultdict(Counter)
for sentence in training:
for word, tag in sentence:
word_tags[word][tag] += 1
def tag_sentence(sentence):
result = []
for word in sentence.lower().split():
tag = word_tags[word].most_common(1)[0][0] if word in word_tags else "NOUN"
result.append((word, tag))
return result
print(tag_sentence("the cat runs"))
