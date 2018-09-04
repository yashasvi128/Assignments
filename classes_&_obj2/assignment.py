#question-1 (Area And Circumference)
class circle:
    def __init__(self, r):
        self.radius = r
    def getArea(self):
        return(3.14*self.radius*self.radius)
    def getCircumference(self):
        return(2*3.14*self.radius)
r = int(input("enter the radius of circle"))
c = circle(r)
print("the area of circle is ",c.getArea())
print("the circumference of circle is ",c.getCircumference())



#question-2
class student:
    def __init__(self):
        self.name = (input("enter your name "))
        self.rollno = int(input("enter rollno "))
    def setAge(self):
        self.age = int(input("enter your age "))
    def setMarks(self):
        self.marks = int(input("enter the  marks "))
    def display(self):
        print("name:",self.name,"\n","rollno:",self.rollno,"\n","age:",self.age,"\n","marks:",self.marks)
s = student()
s.setAge()
s.setMarks()
s.display()




#question-3
class temperature:
    def convertFahrenheit(self):
        self.c = int(input("enter temperature in celsius "))
        return((9/5)*self.c+32)
    def convertCelsius(self):
        self.f = int(input("enter temperature in Fahrenheit "))
        return(((self.f-32)*5)/9)
t = temperature()
print(t.convertFahrenheit())
print(t.convertCelsius())




#question-4
class Movie:
    def __init__(self):
        self.artistname = input("enter artist name :")
        self.year_of_release = input("enter year :")
        self.rating = int(input("enter ratings out of 10 :"))
    def add(self):
        self.movie_name = input("enter the movie name :")
        self.collection = int(input("enter total collection :"))
    def display(self):
        print(self.movie_name)
        print(self.artistname)
        print(self.year_of_release)
        print(self.rating)
        print(self.collection)
m = Movie()
m.add()
m.display()




#question-5
class animal:
    def animal_attribute(self):
        return("print tiger.")
class Tiger(animal):
    pass
t = Tiger()
print(t.animal_attribute())


"""
#question-6
output will be:
A B
A B
"""



#question-7
class shape:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b
    def area(self):
        return(self.length*self.breadth)
class rectangle(shape):
    pass
class square(shape):
    pass
l = int(input("enter the length "))
b = int(input("enter the breadth "))
r = rectangle(l, b)
s = square(l, b)
print("area of rectangle ", r.area())
print("area of square ", s.area())