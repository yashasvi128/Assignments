def table(n):
    for i in range(1,11):
        print(n,'x',i,'=',n*i)

n = int(input("Enter the number whos table you want to print"))
table(n)