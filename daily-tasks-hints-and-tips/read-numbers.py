digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] 
number = input()
for n in str(number):
    print(digits[int(n)])