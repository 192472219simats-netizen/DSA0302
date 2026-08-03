# Stemming Based Preprocessing

words = ["played", "player", "playing"]

print("-" * 90)
print("{:<15}{:<15}{:<15}{:<18}{:<15}".format(
    "Word", "Stem", "Removed", "Type", "Normalized"))
print("-" * 90)

for word in words:

    if word.endswith("ed"):
        stem = word[:-2]
        affix = "ed"
        t = "Inflectional"

    elif word.endswith("ing"):
        stem = word[:-3]
        affix = "ing"
        t = "Inflectional"

    elif word.endswith("er"):
        stem = word[:-2]
        affix = "er"
        t = "Derivational"

    else:
        stem = word
        affix = "-"
        t = "-"

    print("{:<15}{:<15}{:<15}{:<18}{:<15}".format(
        word, stem, affix, t, stem))