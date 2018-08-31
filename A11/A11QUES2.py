import re
phone = input("Enter the valid phone number.")
if re.findall('^[+]{1}[9]{1}[1]{1}[6-9]{1}[0-9]{9}', phone):
    print("valid number")
else:
    print("plz enter a valid phone number")