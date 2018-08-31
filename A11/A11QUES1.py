import re
mail = input("enter a valid email address")
m =  re.finditer('\w[_a-zA-Z0-9.]*(@)(gmail.com|yahoo.com)' , 'mail')
if mail = True:
    print("You may proceed.")
else:
    print("please enter a valid email address")
