sentence = "I love natural language processing"
tokens = sentence.split()
unigrams = [(tokens[i],) for i in range(len(tokens))]
bigrams = [(tokens[i], tokens[i + 1])
for i in range(len(tokens) - 1)]
trigrams = [(tokens[i], tokens[i + 1], tokens[i + 2])
for i in range(len(tokens) - 2)]
print("Tokens:", tokens)
print("Unigrams:", unigrams)
print("Bigrams:", bigrams)
print("Trigrams:", trigrams)
