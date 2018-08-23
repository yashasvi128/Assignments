a = ["hi", 2, 8.45, "wow", 2829, 4.4]
for i in range(len(a)):
    if a[i].isstr():
        l = a.append(input(a[i]))
    elif a[i].isint():
        l1 = a.append(input(a[i]))
    elif a[i].isfloat():
        l2 = a.append(input(a[i]))
print(l)
print(l1)
print(l2)