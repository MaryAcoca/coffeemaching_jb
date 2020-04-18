names_list = []
name = 0

while name != ".":
    name = input()
    names_list.append(name)
    if name == ".":
        names_list.remove(".")
print(names_list)
print(len(names_list))