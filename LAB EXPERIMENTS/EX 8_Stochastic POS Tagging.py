import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from collections import Counter

# Download required packages (Run only once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

# Input sentence
text = input("Enter a sentence: ")

# Tokenize
words = word_tokenize(text)

# POS Tagging
tags = pos_tag(words)

print("\nAssigned POS Tags:")
for word, tag in tags:
    print(f"{word} --> {tag}")

# Count tag frequencies (simple probabilistic model)
tag_count = Counter(tag for word, tag in tags)

print("\nTag Probabilities:")
total = sum(tag_count.values())

for tag, count in tag_count.items():
    probability = count / total
    print(f"{tag}: {probability:.2f}")