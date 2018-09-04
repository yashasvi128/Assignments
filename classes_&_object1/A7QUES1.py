dict = {}
for i in range(int(input("enter the number of elements in the dictionary"))):
    dict[i] = input("enter the value")
search = input("enter the value whos key you want to find ")
for key in dict.keys():
    if dict[key] == search:
        print(key)
        break
else:
    print("Key not found")