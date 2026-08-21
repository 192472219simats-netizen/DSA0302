import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import RegexpTagger

# Download tokenizer (Run only once)
nltk.download('punkt')

# Define rule-based POS tag patterns
patterns = [
    (r'.*ing$', 'VBG'),     # Words ending with 'ing' → Verb (Gerund)
    (r'.*ed$', 'VBD'),      # Words ending with 'ed' → Verb (Past Tense)
    (r'.*es$', 'VBZ'),      # Words ending with 'es' → Verb (3rd Person Singular)
    (r'.*ould$', 'MD'),     # Modal verbs
    (r'.*\'s$', 'NN$'),     # Possessive nouns
    (r'.*s$', 'NNS'),       # Plural nouns
    (r'^[0-9]+$', 'CD'),    # Numbers
    (r'.*', 'NN')           # Default: Noun
]

# Create the tagger
tagger = RegexpTagger(patterns)

# Input sentence
text = input("Enter a sentence: ")

# Tokenize
words = word_tokenize(text)

# Perform rule-based POS tagging
tags = tagger.tag(words)

print("\nRule-Based POS Tags:")
for word, tag in tags:
    print(f"{word} --> {tag}")