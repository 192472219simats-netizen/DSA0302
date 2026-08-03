words = ["writes", "writing", "written"]

print("-"*110)
print("{:<15}{:<35}{:<15}{:<15}{:<15}".format(
    "Word","State Transition","Pattern","Root","Normalized"))
print("-"*110)

for word in words:

    if word == "writes":
        path = "Start -> write -> +s -> End"
        pattern = "Regular"
        root = "write"

    elif word == "writing":
        path = "Start -> write -> +ing -> End"
        pattern = "Regular"
        root = "write"

    elif word == "written":
        path = "Start -> write -> irregular -> End"
        pattern = "Irregular"
        root = "write"

    print("{:<15}{:<35}{:<15}{:<15}{:<15}".format(
        word, path, pattern, root, root))