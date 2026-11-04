import re
tagged = [
("the", "DT"), ("small", "JJ"), ("brown", "JJ"),
("dog", "NN"), ("chased", "VBD"),
("a", "DT"), ("cat", "NN")
]
grammar = r"NP: {<DT>?<JJ>*<NN>}"
try:
import nltk
parser = nltk.RegexpParser(grammar)
tree = parser.parse(tagged)
print(tree)
except ImportError:
print("Install NLTK with: pip install nltk")
print("Tagged tokens:", tagged)
