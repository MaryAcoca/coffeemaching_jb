# several different colutions

# solution 1

count = 0
total = 0
while True:
    number = input()
    if number == ".":
        break
    count += 1
    total += int(number)
print(total / count)

# solution 2 With try/except.

counter = 0
addition = 0

while True:
    try:
        number = int(input())
        addition += number
        counter += 1
    except ValueError:
        break
print(addition / counter)

# solution 3

numbers = []
while True:
    tmp = input()

    if tmp == '.':
        break

    numbers.append(int(tmp))

print(sum(numbers) / len(numbers))