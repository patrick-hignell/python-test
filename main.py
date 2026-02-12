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