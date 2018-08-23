age = int(input("enter your age"))
sex = str(input("enter F if female else enter M for male"))
marital_status = str(input("press y if married else press n for not married"))
if sex == 'F' or sex == 'f':
    print('the employee is female so she will work only in urban areas')
else:
    if age>=20 or age<=40:
        print('the employee is male and is {} years old,so he may work anywhere'.format(age))
    elif age>=40 or age<=60:
        print('the employee is male and is {} years old,so he will work in urban areas'.format(age))
    else:
        print("error")