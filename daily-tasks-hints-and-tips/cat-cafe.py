max_name = ""
max_count = 0

while True:
    current = input()
    if current == "MEOW":
        print(max_name)
        break

    current = current.split()  # name, count
    count = int(current[1])
    if count > max_count:
        max_name = current[0]
        max_count = count



cafes = []
cats = []
while True:
    cafe_cats = input().split()
    if cafe_cats == ['MEOW']:
        break
    cafes.append(cafe_cats[0])
    cats.append(int(cafe_cats[1]))
print(cafes[cats.index(max(cats))])


read = True

names = []
counts = []

while read:
    data = input().split()
    if data[0] == "MEOW":
        break
    names.append(data[0])
    counts.append(int(data[1]))

num = 0
for i in counts:
    if num < i:
        num = i
print(names[counts.index(num)])

