import nltk
tagged_sentence = [
("Students", "NNS"), ("read", "VBP"),
("interesting", "JJ"), ("books", "NNS"),
("in", "IN"), ("the", "DT"), ("library", "NN")
]
grammar = r"""
NP: {<DT>?<JJ>*<NN|NNS>}
"""
chunker = nltk.RegexpParser(grammar)
tree = chunker.parse(tagged_sentence)
print(tree)
print("Noun phrases:")
for subtree in tree.subtrees(lambda t: t.label() == "NP"):
print(" ".join(word for word, tag in subtree.leaves()))
