# solution 1

text = input().split()

for word in text:
    if word.startswith('https://'):
        print(word)
    elif word.startswith('www.'):
        print(word)
    elif word.startswith('WWW.'):
        print(word)
    elif word.startswith('http://'):
        print(word)
    else:
        continue

# solution 2

words = input().split()
for word in words:
    if word.lower().startswith(("https://", "http://", "www.")):
        print(word)

# solution 3

text = input().split()
words = [word for word in text if word.lower().startswith(("www.", "https://", "http://")) is True]
print("\n".join(words))  # finish the code here

