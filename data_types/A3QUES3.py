n = int(input("enter the number of items in the list"))
lst =[]
for i in range(n):
    a = input("enter the element ")
    lst.append(a)
print(lst)
seen = set()
count = 0
for i in lst:
    if i in seen:
        seen.add(i)
        count = count + 1
print(count)