import nltk
from nltk.tokenize import word_tokenize

# Download required NLTK packages (Run only once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

# Input sentence
text = input("Enter a sentence: ")

# Tokenize the sentence
words = word_tokenize(text)

# Perform POS tagging
pos_tags = nltk.pos_tag(words)

print("\nPart-of-Speech Tags:")
for word, tag in pos_tags:
    print(f"{word} --> {tag}")