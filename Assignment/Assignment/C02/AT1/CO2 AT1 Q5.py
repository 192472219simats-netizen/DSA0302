words = ["relational", "relation", "relate"]

print("{:<15}{:<25}{:<20}{:<15}".format(
    "Word", "Applied Rule", "Intermediate", "Final Stem"))

for word in words:

    if word == "relational":
        rule = "Remove 'ational'"
        intermediate = "relate"
        stem = "relat"

    elif word == "relation":
        rule = "Remove 'ion'"
        intermediate = "relat"
        stem = "relat"

    elif word == "relate":
        rule = "Remove 'e'"
        intermediate = "relat"
        stem = "relat"

    print("{:<15}{:<25}{:<20}{:<15}".format(
        word, rule, intermediate, stem))