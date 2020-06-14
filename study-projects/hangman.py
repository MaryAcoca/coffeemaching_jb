import random
print ("H A N G M A N")
print()

word_list = ['python', 'java', 'kotlin', 'javascript']
random_word = random.choice(word_list)

max_guesses = 8
guess = 0
while guess < max_guesses:
    guess +=1
    hint = '-'*len(random_word)
    user_word = 



hint = random_word[0:3]+'-'*(len(random_word)-3)
user_word = input("Guess the word" + hint + ":")
if user_word == random_word:
    print("You survived!")
else:
    print("You are hanged!")
