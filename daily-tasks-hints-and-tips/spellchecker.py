# solution 1

dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

mistake_counter = 0

sentence_input = input().split()

for word in sentence_input:
    if word not in dictionary:
        print(word)
        mistake_counter += 1
    else:
        continue

if mistake_counter == 0:
    print("OK")

# solution 2

dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
string = input().split()
string = [word for word in string if word not in dictionary]
if not string:
    print("OK")
else:
    print("\n".join(string))
