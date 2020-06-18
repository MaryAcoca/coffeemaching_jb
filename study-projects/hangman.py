import random
print ("H A N G M A N")
print()

word_list = ['python', 'java', 'kotlin', 'javascript']
random_word = random.choice(word_list)

max_guesses = 8
guess = 0
hint = '-'*len(random_word)
while guess < max_guesses:
    guess +=1
    print(' '.join(str(elem) for elem in hint))
    letter = input("Input a letter:")
    for i in range(0, len(random_word)):
        if letter == random_word[i]:
            hint[i] = letter
        else:
            print("No such letter in the word")
print("""
Thanks for playing!
We'll see how well you did in the next stage
""")
    