money = int(input())

animals = {
    'sheep': 6769,
    'cow': 3848,
    'pig': 1296,
    'goat': 678,
    'chicken': 23
}

for animal in animals:
    amount = money // animals[animal]
    plural_form = (amount > 1 and animal != 'sheep') * 's'

    if amount > 0:
        print(f"{amount} {animal}{plural_form}")
        break
else:
    print(None)