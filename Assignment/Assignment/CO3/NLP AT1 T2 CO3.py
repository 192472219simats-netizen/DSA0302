import re
from collections import Counter



corpus = """
The student is reading a book.
The student is studying computer science.
The student is learning Python.
The student is writing a program.
The student is attending the class.
The student is preparing for an examination.
The student is solving a problem.
The teacher is helping the student.
The teacher is explaining the lesson.
The teacher is teaching computer science.
The computer is running a program.
The computer is processing the data.
The program is written in Python.
The student is practicing programming.
"""


def preprocess(text):

    text = text.lower()

    sentences = re.split(r'[.!?]+', text)

    result = []

    for sentence in sentences:

        words = re.findall(r'\b[a-z]+\b', sentence)

        if words:
            result.append(
                ["<START>"] + words + ["<END>"]
            )

    return result


sentences = preprocess(corpus)

unigram = Counter()
bigram = Counter()
trigram = Counter()

for sentence in sentences:

    unigram.update(sentence)

    for i in range(len(sentence)-1):
        bigram[
            (sentence[i], sentence[i+1])
        ] += 1

    for i in range(len(sentence)-2):
        trigram[
            (sentence[i], sentence[i+1], sentence[i+2])
        ] += 1


total = sum(unigram.values())


def unigram_prob(word):

    return unigram[word] / total if unigram[word] else 0


def bigram_prob(previous, word):

    count = bigram[(previous, word)]

    denominator = unigram[previous]

    return count / denominator if denominator else 0


def trigram_prob(w1, w2, word):

    count = trigram[(w1, w2, word)]

    denominator = bigram[(w1, w2)]

    return count / denominator if denominator else 0

def backoff_probability(w1, w2, word):

    p3 = trigram_prob(w1, w2, word)

    if p3 > 0:
        return p3, "Trigram"

    p2 = bigram_prob(w2, word)

    if p2 > 0:
        return p2, "Bigram"

    p1 = unigram_prob(word)

    return p1, "Unigram"

lambda1 = 0.2
lambda2 = 0.3
lambda3 = 0.5


def interpolation_probability(w1, w2, word):

    p1 = unigram_prob(word)
    p2 = bigram_prob(w2, word)
    p3 = trigram_prob(w1, w2, word)

    probability = (
        lambda1 * p1 +
        lambda2 * p2 +
        lambda3 * p3
    )

    return probability

vocabulary = list(unigram.keys())


def predict(sentence, method):

    words = re.findall(
        r'\b[a-z]+\b',
        sentence.lower()
    )

    if len(words) < 2:
        return []

    w1 = words[-2]
    w2 = words[-1]

    predictions = []

    for word in vocabulary:

        if word in ["<START>"]:
            continue

        if method == "unsmoothed":

            probability = trigram_prob(
                w1, w2, word
            )

        elif method == "backoff":

            probability, source = backoff_probability(
                w1, w2, word
            )

        elif method == "interpolation":

            probability = interpolation_probability(
                w1, w2, word
            )

        predictions.append(
            (word, probability)
        )

    predictions.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return predictions[:5]




print("N-GRAM PREDICTION SYSTEM")
print("========================")

sentence = input(
    "Enter a sentence/query: "
)

for method in [
    "unsmoothed",
    "backoff",
    "interpolation"
]:

    print(
        "\n---",
        method.upper(),
        "---"
    )

    predictions = predict(
        sentence,
        method
    )

    for word, probability in predictions:

        print(
            f"{word:15} "
            f"{probability:.6f}"
        )
