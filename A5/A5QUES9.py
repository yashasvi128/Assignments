a = ["hi", 2, 8.45, "wow", 2829, 4.4]
l = []
l1 =[]
l2 =[]
for i in a:
    if (type(i)==int):
        l.append(i)
    elif (type(i)==str):
        l1.append(i)
    else:
        l2.append(i)
print(l)
print(l1)
print(l2)