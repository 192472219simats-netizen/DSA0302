# Morphological Analysis Pipeline

words = ["connected", "connecting", "connection"]

print("-" * 80)
print("{:<15}{:<20}{:<18}{:<15}".format("Word", "Parsed Structure", "Type", "Normalized"))
print("-" * 80)

for word in words:

    if word.endswith("ed"):
        root = word[:-2]
        suffix = "ed"
        mtype = "Inflectional"

    elif word.endswith("ing"):
        root = word[:-3]
        suffix = "ing"
        mtype = "Inflectional"

    elif word.endswith("ion"):
        root = word[:-3]
        suffix = "ion"
        mtype = "Derivational"

    else:
        root = word
        suffix = "-"
        mtype = "-"

    # Normalize
    if root.endswith("connect"):
        normalized = "connect"
    elif root == "connect":
        normalized = "connect"
    else:
        normalized = "connect"

    parsed = root + " + " + suffix

    print("{:<15}{:<20}{:<18}{:<15}".format(word, parsed, mtype, normalized))