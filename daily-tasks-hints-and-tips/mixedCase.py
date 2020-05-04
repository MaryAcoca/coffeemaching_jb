# Solution 1

sentence = input().title().split()
print(sentence[0].lower() + "".join(sentence[1:]))

# solution 2

string = input().split()
for counter in enumerate(string[1:]):
    string[counter[0] + 1] = string[counter[0] + 1].title()
print(*string, sep='')

# solution 3

x = [elem.capitalize() for elem in input().split()]
x[0] = x[0].lower()
print("".join(x))

# solution 4

line = input()

words = [word.capitalize() if i > 0 else word
         for i, word in enumerate(line.split())]

print("".join(words))

# solution 5

a = input().title().split()
b = a[0]
b = b.lower()
a.pop(0)
a = "".join(a)
print(f"{b}{a}")
