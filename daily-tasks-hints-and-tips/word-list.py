# solution one

text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]
number = int(input())

list_of_words = [x for sublist in text for x in sublist if len(x) <= number]
print (list_of_words)

# same but with better variables

text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]

inpt = int(input())
print([word for group in text for word in group if len(word) <= inpt])