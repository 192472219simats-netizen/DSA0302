import nltk
from nltk.util import bigrams

# Download tokenizer (Run only once)
nltk.download('punkt')

# Input text
text = input("Enter a sentence: ")

# Tokenize the text
words = nltk.word_tokenize(text)

# Generate bigrams
bigram_list = list(bigrams(words))

print("\nGenerated Bigrams:")
for bg in bigram_list:
    print(bg)