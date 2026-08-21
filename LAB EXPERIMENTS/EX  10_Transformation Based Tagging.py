import nltk
from nltk.tokenize import word_tokenize

# Download required package (Run only once)
nltk.download('punkt')

# Input sentence
text = input("Enter a sentence: ")

# Tokenize the sentence
words = word_tokenize(text)

print("\nTransformation-Based POS Tags:")

# Apply simple transformation rules
for word in words:
    if word.endswith("ing"):
        tag = "VBG"      # Verb (Gerund)
    elif word.endswith("ed"):
        tag = "VBD"      # Verb (Past Tense)
    elif word.endswith("ly"):
        tag = "RB"       # Adverb
    elif word.endswith("s"):
        tag = "NNS"      # Plural Noun
    elif word[0].isupper():
        tag = "NNP"      # Proper Noun
    else:
        tag = "NN"       # Default Noun

    print(f"{word} --> {tag}")