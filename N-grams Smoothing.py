from collections import Counter
sentences = ["I love NLP", "I love Python", "I study NLP"]
unigrams = Counter()
bigrams = Counter()
for sentence in sentences:
tokens = sentence.lower().split()
unigrams.update(tokens)
bigrams.update(zip(tokens, tokens[1:]))
vocab = set(unigrams)
V = len(vocab)
def laplace_probability(previous, current):
numerator = bigrams[(previous, current)] + 1
denominator = unigrams[previous] + V
return numerator / denominator
print("Vocabulary size:", V)
print("P(love | i):", round(laplace_probability("i", "love"), 3))
print("P(python | love):", round(laplace_probability("love", "python"), 3))
print("P(study | you):", round(laplace_probability("you", "study"), 3))
