# work with a list from this variable
numbers = [int(n) for n in input()]

# change the next two lines
less_than_5 = [num for num in numbers if num < 5]
greater_than_5 = [num for num in numbers if num > 5]
# printing your results
print(less_than_5)
print(greater_than_5)

# work with a list from this variable
numbers = [int(n) for n in input()]

# change the next two lines
less_than_5 = []
x = [less_than_5.append(x) for x in numbers if x < 5 ]
greater_than_5 = []
y = [greater_than_5.append(y) for y in numbers if y > 5 ]

# printing your results
print(less_than_5)
print(greater_than_5)
