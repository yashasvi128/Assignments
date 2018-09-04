import re
mail = input("enter a valid email address")
if re.finditer('\w[_a-zA-Z0-9.]*(@)(gmail.com|yahoo.com)', mail):
    print("You may proceed.")
else:
    print("please enter a valid email address")