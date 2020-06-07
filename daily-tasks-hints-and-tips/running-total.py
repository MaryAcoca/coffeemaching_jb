list1 = [int(n) for n in input()]
s = 0
list2 = []
for n in list1:
    s += n
    list2.append(s)
print(list2)


def Cumulative(lists):  
    cu_list = []  
    length = len(lists)  
    cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)]  
    return cu_list[1:] 
  
digital = input()
lists = [int(d) for d in str(digital)]  
print (Cumulative(lists))


digits = [int(ch) for ch in input()]
total = []
temp_var = 0
for digit in digits:
    elem = temp_var + digit
    temp_var = elem
    total.append(elem)
print(total)