student = {"feen":{"Social":80,"Science":85,"English":83},
            "yeen":{"Social":87,"Science":76,"English":90}}
Name = input("Enter the name of student: ")
if Name in student:
    print(Name)
    for key,value in student[Name].items():
        print(key,value)
else:
    print("Student not found")