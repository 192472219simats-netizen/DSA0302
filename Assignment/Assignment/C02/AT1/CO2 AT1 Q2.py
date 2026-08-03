# Morphological Parsing

words = ["unhappy", "happiness", "happily"]

print("-" * 90)
print("{:<15}{:<10}{:<10}{:<12}{:<18}{:<15}".format(
    "Word", "Prefix", "Root", "Suffix", "Type", "Normalized"))
print("-" * 90)

for word in words:

    prefix = "-"
    suffix = "-"
    root = ""

    if word.startswith("un"):
        prefix = "un"
        root = "happy"
        suffix = "-"
        mtype = "Derivational"

    elif word.endswith("ness"):
        prefix = "-"
        root = "happy"
        suffix = "ness"
        mtype = "Derivational"

    elif word.endswith("ly"):
        prefix = "-"
        root = "happy"
        suffix = "ly"
        mtype = "Derivational"

    print("{:<15}{:<10}{:<10}{:<12}{:<18}{:<15}".format(
        word, prefix, root, suffix, mtype, "happy"))