import re
import math
from collections import Counter

train_corpus = """
The student is reading a book.
The student is studying computer science.
The student is learning Python.
The student is writing a program.
The teacher is helping the student.
The teacher is explaining the lesson.
The student is attending the class.
The computer is running a program.
The program is written in Python.
"""
test_corpus = """
The student is reading a book.
The teacher is helping the student.
The student is playing football.
The computer is running a program.
"""

def preprocess(text):

    text = text.lower()

    sentences = re.split(r'[.!?]+', text)

    result = []

    for sentence in sentences:

        words = re.findall(
            r'\b[a-z]+\b',
            sentence
        )

        if words:

            result.append(
                ["<START>"] + words + ["<END>"]
            )

    return result


train = preprocess(train_corpus)
test = preprocess(test_corpus)

unigram = Counter()
bigram = Counter()
trigram = Counter()

for sentence in train:

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

def probability(sentence, n):

    log_probability = 0
    word_count = 0

    for i in range(len(sentence)):

        word = sentence[i]

        if n == 1:

            count = unigram[word]

            if count == 0:
                return float("inf")

            p = count / total

        elif n == 2:

            if i == 0:
                continue

            previous = sentence[i-1]

            count = bigram[
                (previous, word)
            ]

            denominator = unigram[previous]

            if count == 0:
                return float("inf")

            p = count / denominator

        else:

            if i < 2:
                continue

            w1 = sentence[i-2]
            w2 = sentence[i-1]

            count = trigram[
                (w1, w2, word)
            ]

            denominator = bigram[
                (w1, w2)
            ]

            if count == 0:
                return float("inf")

            p = count / denominator

        log_probability += math.log2(p)

        word_count += 1

    if word_count == 0:
        return float("inf")

    entropy = -log_probability / word_count

    return entropy


for n in [1, 2, 3]:

    print("\n" + "=" * 60)
    print(f"{n}-GRAM ENTROPY")
    print("=" * 60)

    for sentence in test:

        h = probability(
            sentence,
            n
        )

        print(
            " ".join(sentence[1:-1]),
            "=>",
            h
        )
