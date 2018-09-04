#question-1
# --> ZeroDivisionError
a=3
if a<4:
    try:
        a=a/(a-3)
    except:
        print("denominator can't be zero!")
print(a)



#question-2
# --> IndexError
l=[1,2,3]
try:
    print(l[3])
except:
    print("indexes above 2 aren't acceptable.")




#question-3
# --> An exception
# --> error


#question-4
# --> -5.0
# --> a/b result in 0


#question-5
# 1.IMPORT ERROR
try:
    import copyy
except ImportError as message:
    print('Exception:', message)
# 2.VALUE ERROR
try:
    num = int(input("enter a number :"))
except ValueError as message:
    print('Exception:', message)
# 3.INDEX ERROR
l = [1,2,3]
try:
    print(l[3])
except:
    print("indexes above 2 aren't acceptable.")
