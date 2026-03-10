# #This is my first Python program
# print("I like pizza!")
# print("It's really good!")

# first_name = "Patrick"
# food = "pizza"
# email = "Bro123@fake.com"

# age = 25
# quantity = 3

# is_student = True

# print(f"Hello {first_name}")
# print(f"You like {food}")
# print(f"your email is {email}")
# print(f"you are {age} years old")
# print(f"you are buying {quantity} of products")

# print(f"are you a student? {is_student}")

# if is_student:
#   print("you are a student")
# else:
#   print("you are not a student")

# print(type(first_name))

# print(float(age))

# age += 1

# print(str(age))

# username = ""

# print(bool(username))

# your_name = input("What is your name?: ")

# print(f"Nice to meet you {your_name}")

# your_age = int(input("What is your age?: "))

# your_age += 1
# print(f"Happy Birthday {your_name}! you are now {your_age} years old!")

# import math

# a = float(input("side a length: "))
# b = float(input("side b length: "))

# c = math.sqrt(pow(a,2) + pow(b,2))

# print(f"side c length: {c}")

# test = "*"
# result = test.isnumeric()
# print(result)


# a = input("input a number: ")

# if not a.isnumeric():
#   print('that is not a valid number')
# else:
#   result = "even" if float(a) % 2 == 0 else "odd"
#   print(f"{a} is an {result} number")

# word = input("input a word: ")
# letter = input("input a letter: ")

# if letter not in word:
#   print(f"{word} does not contain the letter {letter}")
# else:
#   letter_count = word.count(letter)
#   print(f"{word} contains the letter {letter} {letter_count} time{"s" if letter_count > 1 else ""}")
#   first_occurance = word.find(letter)
#   last_occurance = word.rfind(letter)
#   print(f"the letter {letter} {"first " if letter_count > 1 else ""}occurs in {word} at position {first_occurance}{f", it occurs last at position {last_occurance}" if letter_count > 1 else ""}")

# name = input('what is your name?: ')
# print(name.lower())
# print(name.capitalize())
# print(name.upper())
# print(name.isdigit()) # is false if any letters, spaces or punctuation (including decimal place!)
# print(name.isalpha()) # is false if any numbers, spaces or punctuation
# print("what a pretty name!")

# indexing a string- STRING_EXAMPLE[start:end:step]

# credit_number = "1234-5678-90123-3456"

# print(credit_number[0]) # prints "1"
# print(credit_number[5:9]) # prints "5678" - end is exclusive
# print(credit_number[:4]) # prints "1234" - if no starting index, it assumes you are starting from the start
# print(credit_number[4:]) # prints "-5678-90123-3456" - if no ending index, it assumes you are ending at the end
# print(credit_number[-1]) # prints "6" - negatives start at end of string
# print(credit_number[-4]) # prints "3"
# print(credit_number[::2]) # prints "13-6891335" step by 2 will print every other character

# last_four_digits = credit_number[-4:]

# print(last_four_digits)

# reverse_string = credit_number[::-1]

# print(reverse_string)

#format specifiers
# order - [[fill]align][sign][#][0][minimumwidth][.precision][type]

# :<		Left aligns the result (within the available space)
# :>		Right aligns the result (within the available space)
# :^		Center aligns the result (within the available space)
# :=		Places the sign to the left most position
# :+		Use a plus sign to indicate if the result is positive or negative
# :-		Use a minus sign for negative values only
# : 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
# :,		Use a comma as a thousand separator
# :_		Use a underscore as a thousand separator
# :b		Binary format
# :c		Converts the value into the corresponding Unicode character
# :d		Decimal format
# :e		Scientific format, with a lower case e
# :E		Scientific format, with an upper case E
# :f		Fix point number format
# :F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
# :g		General format
# :G		General format (using a upper case E for scientific notations)
# :o		Octal format
# :x		Hex format, lower case
# :X		Hex format, upper case
# :n		Number format
# :%		Percentage format

# price1 = 3000.14159
# price2 = -9870.65
# price3 = 1200.34

# print(f"Price 1 is ${price1:+10,.2f}")
# print(f"Price 2 is ${price2:+10,.2f}")
# print(f"Price 3 is ${price3:+10,.2f}")

#while loop

# name = input("Enter your name: ")

# while name == "":
#   print("You did not enter your name")
#   name = input("Enter your name: ")

# print(f"Hello {name}")

# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#   print (f"you like {food}")
#   food = input("Enter another food you like (q to quit): ")

# print("bye")

# compound interest calculator

# principle = 0
# rate = 0
# time = 0

# while True:
#   try:
#     principle = float(input("Enter the principle amount: "))
#   except:
#     print ("Amount must be a number")
#     continue
#   if principle < 0:
#     print ("principle can't be less than zero")
#   else:
#     break

# while True:
#   try:
#     rate = float(input("Enter the rate amount: "))
#   except:
#     print ("Amount must be a number")
#     continue
#   if rate < 0:
#     print ("rate can't be less than zero")
#   else:
#     break

# while True:
#   try:
#     time = float(input("Enter the time amount: "))
#   except:
#     print ("Amount must be a number")
#     continue
#   if time < 0:
#     print ("time can't be less than zero")
#   else:
#     break

# total = principle * pow((1+ rate / 100), time)

# print (f"Balance after {time:g} year/s: ${total:.2f}")

# for x in reversed(range(1,11)):
#   print(x)

# print("HAPPY NEW YEAR!  ")

# print("Odd numbers:")
# for x in (range(1,11,2)):
#   print(x)

# import time
# my_time = int(input("Enter the time in seconds: "))

# for x in range(my_time, 0, -1):
#   print(x)
#   time.sleep(1)

# print("Time's up!")

# import time
# my_time = int(input("Enter the time in seconds: "))

# for x in range(my_time, 0 , -1):
#   seconds = x % 60
#   minutes = int(x/60) % 60
#   hours = int (x/3600)
#   print(f"{hours:02}:{minutes:02}:{seconds:02}")
#   time.sleep(1)

# print("TIME'S UP!")

# for x in range(1, 10):
#   print (x, end="") # puts all numbers on the same line as end is changed form new line to ""

# collection = single "variable" used to store multiple values
# - list = [] ordered and changable. duplicates ok
# - set - {} unordered and immutable, but add/remove ok, no duplicates
# - tuple = () ordered and unchangable. duplicates ok. faster

# dictionaries

# capitals = {"USA": "Washington D.C.",
#             "India": "New Delhi",
#             "China" : "Beijing",
#             "Russia" : "Moscow"}

# print(capitals.get("India")) # prints "New Delhi"

# print(capitals.get("Japan")) # prints "none"

# capitals.update({"Germany":"Berlin"})
# capitals.update({"USA":"Neo Yokio"})

# capitals.pop("China")
# capitals.popitem() # removes the last item

# print(capitals)
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

# for key, value in capitals.items():
#   print(f"{key}: {value}")

#random
# import random
# cards = ["2","3","4","5","6","7","8","9","10","J","Q","K"]
# random.shuffle(cards)

# print(cards)

#Function arguments order-
# 1 - positional (normal)
# 2 - keyword greeting(title = "Mr.")
# 3 - default def time(factor = 0)
# 4 - arbitrary - args THEN kwargs

# def hello (greeting, first, last, ending = "nice to meet you"):
#   print(f"{greeting}, {first} {last}. {ending}")

# hello("hello",last="Squarepants",first="Spongebob")

# print("1","2","3","4","5",sep="-")

# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
# *unpacking operator

# def add(*nums):
#   total = 0
#   for num in nums:
#     total = total + num
#   return total

# print(add(1,2,3))

# def print_address(**kwargs):
#   for key, value in kwargs.items():
#     print(f"{key}: {value}")

# print_address(street="123 Fake St.",
#       city="Inventedopolis",
#       state="NA",
#       zip="6969")

# def shipping_label(*args,**kwargs):
#   for arg in args:
#     print(arg, end=" ")
#   print()

#   print(f"{kwargs.get('street')}{f" {kwargs.get('apt')}" if "apt" in kwargs else ""}")
#   print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

# shipping_label("Dr.", "Spongebob", "Squarepants", street="123 Fake St.",
#       city="Inventedopolis",
#       state="NA",
#       zip="6969")

# shipping_label("Dr.", "Spongebob", "Squarepants", street="123 Fake St.", apt="#100",
#       city="Inventedopolis",
#       state="NA",
#       zip="6969")

# List comprehension
# [expression for value in iterable if condition]

# doubles = [x * 2 for x in range(1, 11)]
# triples = [x * 3 for x in range(1, 11)]
# squares = [x * x for x in range(1, 11)]

# print(doubles)
# print(triples)
# print(squares)

# fruits = ["apple", "orage", "banana", "coconut"]
# fruits = [fruit.upper() for fruit in fruits]

# print(fruits)

# fruit_chars = [fruit[0] for fruit in fruits]

# print(fruit_chars)

# numbers = [1,-2,3,-4,5,-6]


# pos_nums = [num for num in numbers if num >=0]

# print(pos_nums)

# num_string = ", ".join([str(num) for index, num in enumerate(numbers) if index < len(numbers) -1])
# num_string += f"{" and " if len(numbers) > 1 else ""}{numbers[-1]}"

# print(num_string)


# switch statements-

# def day_of_week(day):
#   match day:
#     case "1":
#       return "Monday"
#     case "2":
#       return "Tuesday"
#     case "3":
#       return "Wednesday"
#     case "4":
#       return "Thursday"
#     case "5":
#       return "Friday"
#     case "6":
#       return "Saturday"
#     case "7":
#       return "Sunday"
#     case _:
#       return "Invalid Day"
    
# def is_weekend(day):
#   match day:
#     case "Saturday" | "Sunday":
#       return True
#     case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#       return False
#     case _:
#       return False
    
# response = input("week day number: ")
# print(day_of_week(response))
# print("Have a good weekend!") if is_weekend(day_of_week(response)) else ""

#modules

# import math

# print(math.pi)

# import math as m

# print(m.pi)

# from math import pi

# print(pi)

# import module_example

# module_example.i_like("bananas")

# module_example.i_dont_like("pineapple")


#scope respolution = (LEGB) Local -> Enclosed -> Global -> Built-in


#if __name__ == '__main__':
# main()

#Python Object Orientated Programming-
# class

# class Car:
#   def __init__(self, model, year, color, for_sale):
#     self.model = model
#     self.year = year
#     self.color = color
#     self.for_sale = for_sale

#   def describe(self):
#     print(f"A {self.year} {self.color} {self.model}. It is {"" if self.for_sale else "not "}for sale")

#   def drive(self):
#     print(f"You drive the {self.color} {self.model}")
  
#   def stop(self):
#     print(f"You stop the {self.color} {self.model}")

# car1 = Car("Toyota Corolla", 2003,"silver",False)

# car1.describe()

# car1.drive()

# car1.stop()


#class variables
#class variables vs instance variables- all instances of a class share class variables. Each instance has different instance variables.
#class variables are defined outside of the constructor (no self)

# class Student:

#   class_year = 2024
#   num_students = 0
  
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age
#     Student.num_students += 1



# student1 = Student("Spongebob",30)

# student2 = Student("Patrick",35)

# print(student1.name)
# print(student1.class_year)
# print(Student.class_year) #preferrable to get class variables from the class itself to make it explicit that it is a class variable

# print(student1.num_students) #will be the same
# print(Student.num_students)


#Inheritance

# class Animal:
#   def __init__(self, name):
#     self.name = name
#     self.is_alive = True
  
#   def eat(self):
#     print(f"{self.name} is eating")

#   def sleep(self):
#     print(f"{self.name} is sleeping")

# class Dog(Animal):
#   def speak(self):
#     print("Woof!")

# class Cat(Animal):
#  def speak(self):
#     print("Meow!")

# class Mouse(Animal):
#   def speak(self):
#     print("Squeak!")

# dog = Dog("Scooby")
# cat = Cat("Garfield")
# mouse = Mouse("Mickey")

# print(dog.name)

# dog.sleep()

# dog.speak()


# multiple inheritance = inherit from more than one parent- C(A,B)
# multilevel inheritance = inherit from a parent which inherits from anothe rparent C(B) <- B(A) <- A

# class Animal:

#   def __init__(self,name):
#     self.name = name

#   def eat(self):
#     print(f"{self.name} is eating")
  
#   def sleep(self):
#     print(f"{self.name} is sleeping")

# class Prey(Animal):
#   def flee(self):
#     print(f"{self.name} is fleeing")

# class Predator(Animal):
#   def hunt(self):
#     print(f"{self.name} is hunting")

# class Rabbit(Prey):
#   pass

# class Hawk(Predator):
#   pass

# class Fish(Prey, Predator):
#   pass

# hawk = Hawk("Tony")

# hawk.hunt()

# hawk.eat()


#super()- function used in a child class to call methods from a parent class (superclass)
# import math
# class Shape:
#   def __init__(self, color, is_filled):
#     self.color = color
#     self.is_filled = is_filled

#   def describe(self):
#     print(f"It is {self.color} and {"filled" if self.is_filled else "not filled"}")

# class Circle(Shape):
#   def __init__(self, color, is_filled, radius):
#     super().__init__(color,is_filled)
#     self.radius = radius

#   def describe(self):
#     print(f"It is a circle with an area of {math.pi * self.radius * self.radius:.2f}cm^2")
#     super().describe()
# class Square(Shape):
#   def __init__(self, color, is_filled, width):
#     super().__init__(color,is_filled)
#     self.width = width

# class Triangle(Shape):
#   def __init__(self, color, is_filled, width, height):
#     super().__init__(color, is_filled)
#     self.width = width
#     self.height = height

# circle = Circle("red",True,5)

# print(circle.color)
# circle.describe()

# abstract methods- a method declared in an abstract base class (ABC) that has no implementation. Allows for polymorphism
# It acts as a blueprint, enforcing a specific interface that all non-abstract subclasses must implement, or an error will be raised upon instantiation. 
# requries importing-

# from abc import ABC, abstractmethod


# duck typing- achieves polymorphism without inheritance. so long as it has the same methods, can be treated the same in for loops etc.
# if it quacks like a duck....


#static methods- a method that belongs to a class rather than any object from that class- uses decorator @staticmethod

# class Employee:
#   def __init__(self, name, position):
#     self.name = name
#     self.position = position

#   def get_info(self):
#     return f"{self.name} = {self.position}"
  
#   @staticmethod
#   def is_valid_position(position):
#     valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
#     return position in valid_positions

# employee1 = Employee("Spongebob", "Cook")
# employee2 = Employee("Sandy", "Rocket Scientist")

# print(employee1.get_info())
# print(Employee.is_valid_position(employee1.position))

# print(employee2.get_info())
# print(Employee.is_valid_position(employee2.position))


# Class methods - Allow operations related to the class itself
#               - Take (cls) as the first parameter, which represents the class itself

# instance methods- best for operations on instances of the class (objects
# static methods- best for utility functions that do not need access to class data
# class methods - best for class-level data or require access to the class itself

# class Student:
#   count = 0
#   total_gpa = 0

#   def __init__(self, name, gpa):
#     self.name = name
#     self.gpa = gpa
#     Student.count += 1
#     Student.total_gpa += gpa

#   #INSTANCE METHOD
#   def get_info(self):
#     return f"{self.name} {self.gpa}"
  
#   @classmethod
#   def get_count(cls):
#     return f"Total # of students: {cls.count}"
  
#   @classmethod
#   def get_average_gpa(cls):
#     if cls.count == 0:
#       return 0
#     else:
#       return f"Average gpa: {cls.total_gpa / cls.count:.2f}"

  
# student1 = Student("Spongebob", 3.2)
# student2 = Student("Patrick", 2.0)
# student3 = Student("Sandy",4.0)

# print(Student.get_count())
# print(Student.get_average_gpa())


# Magic methods - Dunder methods (double underscore) __init__, __str__, __eq__
#               - They are automatically called by many of Python's built-in operations
#               - They allow developers to define or customize the behaviour of objects


class Book:

  def __init__(self, title, author, num_pages):
    self.title = title
    self.author = author
    self.num_pages = num_pages

  def __str__(self):
    return f"'{self.title}' by {self.author}"
  
  def __eq__(self, other):
    return self.title == other.title and self.author == other.author
  
  def __lt__(self,other):
    return self.num_pages < other.num_pages
  
  def __gt__(self,other):
    return self.num_pages > other.num_pages
  
  def __add__(self,other):
    return self.num_pages + other.num_pages
  
  def __contains__(self,keyword):
    return keyword in self.title or keyword in self.author
  
  def __getitem__(self,key):
    if key == "title":
      return self.title
    elif key == "author":
      return self.author
    elif key == "num_pages":
      return self.num_pages
    else:
      return f"Key '{key}' was not found"

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)

print(book1)
print(book1 == book2)
print(book1 < book2)
print(book2 > book3)
print(book1 + book3)
print("Lion" in book3)
print(book2["title"])
print(book2["audio"])