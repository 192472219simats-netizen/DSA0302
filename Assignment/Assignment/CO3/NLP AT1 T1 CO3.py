import re
from collections import Counter


corpus = """
The student is reading a book.
The student is studying computer science.
The student is learning Python.
The student is writing a program.
The student is attending the class.
The student is preparing for an examination.
The student is using a computer.
The student is solving a problem.
The teacher is helping the student.
The teacher is explaining the lesson.
The teacher is teaching computer science.
The teacher is checking the assignment.
The computer is running a program.
The computer is processing the data.
The program is written in Python.
The student is practicing programming.
"""


def preprocess(text):
    text = text.lower()

    sentences = re.split(r'[.!?]+', text)

    tokenized = []

    for sentence in sentences:
        words = re.findall(r'\b[a-z]+\b', sentence)

        if words:
            words = ["<START>"] + words + ["<END>"]
            tokenized.append(words)

    return tokenized


sentences = preprocess(corpus)


def generate_ngrams(sentences, n):

    counts = Counter()

    for sentence in sentences:

        for i in range(len(sentence) - n + 1):

            ngram = tuple(sentence[i:i+n])
            counts[ngram] += 1

    return counts


unigrams = generate_ngrams(sentences, 1)
bigrams = generate_ngrams(sentences, 2)
trigrams = generate_ngrams(sentences, 3)

def calculate_probability(ngram, n):

    if n == 1:

        total = sum(unigrams.values())

        return unigrams[ngram] / total if unigrams[ngram] else 0

    elif n == 2:

        word = (ngram[0],)

        return (
            bigrams[ngram] / unigrams[word]
            if unigrams[word] and bigrams[ngram]
            else 0
        )

    elif n == 3:

        prefix = (ngram[0], ngram[1])

        return (
            trigrams[ngram] / bigrams[prefix]
            if bigrams[prefix] and trigrams[ngram]
            else 0
        )



def display_model(n):

    if n == 1:
        model = unigrams

    elif n == 2:
        model = bigrams

    else:
        model = trigrams

    print("\n" + "=" * 60)
    print(f"{n}-GRAM FREQUENCY AND PROBABILITY")
    print("=" * 60)

    for ngram, count in model.items():

        probability = calculate_probability(ngram, n)

        print(
            f"{' '.join(ngram):35} "
            f"Count = {count:<3} "
            f"Probability = {probability:.4f}"
        )



def predict_next_word(sentence, n):

    words = re.findall(r'\b[a-z]+\b', sentence.lower())

    predictions = []

    if n == 1:

        for ngram, count in unigrams.items():

            word = ngram[0]

            probability = count / sum(unigrams.values())

            predictions.append((word, probability))

    elif n == 2:

        if not words:
            return []

        previous = words[-1]

        for ngram, count in bigrams.items():

            if ngram[0] == previous:

                probability = count / unigrams[(previous,)]

                predictions.append((ngram[1], probability))

    elif n == 3:

        if len(words) < 2:
            return []

        previous_two = tuple(words[-2:])

        for ngram, count in trigrams.items():

            if ngram[:2] == previous_two:

                probability = count / bigrams[previous_two]

                predictions.append((ngram[2], probability))

    predictions.sort(key=lambda x: x[1], reverse=True)

    return predictions[:5]

def check_unseen_ngram():

    test = ("student", "plays", "football")

    probability = calculate_probability(test, 3)

    print("\nUnseen Trigram:")
    print(test)

    print("Probability =", probability)



def evaluate(test_sentences, n):

    correct = 0
    total = 0

    print("\n" + "=" * 60)
    print(f"EVALUATION FOR N = {n}")
    print("=" * 60)

    for sentence in test_sentences:

        words = sentence.lower().split()

        if n == 3 and len(words) >= 3:

            context = " ".join(words[:-1])
            actual = words[-1]

        elif n == 2 and len(words) >= 2:

            context = words[-2]
            actual = words[-1]

        else:
            continue

        predictions = predict_next_word(context, n)

        predicted_words = [word for word, _ in predictions]

        print("\nSentence:", sentence)
        print("Actual next word:", actual)
        print("Predictions:", predicted_words)

        if actual in predicted_words:
            correct += 1

        total += 1

    accuracy = correct / total if total else 0

    print("\nTop-5 Accuracy =", round(accuracy * 100, 2), "%")



print("N-GRAM LANGUAGE MODEL")
print("=====================")

print("\nSelect N:")
print("1 - Unigram")
print("2 - Bigram")
print("3 - Trigram")

n = int(input("Enter N: "))

if n not in [1, 2, 3]:

    print("Invalid N")

else:

    display_model(n)

    sentence = input("\nEnter incomplete sentence: ")

    predictions = predict_next_word(sentence, n)

    print("\nTop-5 Next Word Predictions:")

    for word, probability in predictions:

        print(
            f"{word:15} "
            f"Probability = {probability:.4f}"
        )

    check_unseen_ngram()

    test_data = [
        "The student is reading",
        "The student is studying",
        "The teacher is helping"
    ]

    evaluate(test_data, n)
