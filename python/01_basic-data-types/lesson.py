# Data Types: Int, Float, String, Bool, Datetime

# Read the following before starting
# Automate The Boring Stuff With Python - Pages 14 to 28
# Python All in One For Dummies - Pages 85 to 123
# Python Crash Course - Pages 19 to 36

# Do the Practice Questions in Automate The Boring Stuff With Python - Pages 28 - 29

# ADDITIONAL LESSONS

# 1. Basic Data Types
# 1.a) Number Types
x = 34 # Integer Type
y1 = 4 # Integer Type
y2 = 4.0 # Float Type

# What are the difference between both divisions statements? Why is that?
# Bonus: Run the below using Python2 and Python 3
print(x / y1)
print(x / y2)

# What are the difference between both multiplication statements? Why is that?
# Bonus: Run the below using Python2 and Python 3
print(x * y1)
print(x * y2)

# 1.b) String Type
# Create a string variable 'name' that will be used in the print statement below.
name = 0
print(f'Welcome to {name} python code')

# 2. Data type conversion
z1 = 16
z2 = 3.14
z3 = "8"

# 2.a) Print the types of z1, z2, z3.
# 2.b) Convert z1 to a float and z3 into an integer.

# 3. String Manipulation
a = "hello there"
b = "Goodbye now"
c = ""

# 3.a) Print the number of characters in each of these strings.

# 3.b) Strings in Python are *immutable*. They can't be changed once created.
print(a.replace("there", "friend"))
print(a)                              # Does not change the original string.
# Using replace(), how can you change the string in "a" to say "hello friend"?

# 3.c) Print the 3rd character of "a" and "b". What happens when you try the same on c?

# 4. Boolean
# Booleans only take on two values: True or False
is_happy = True
is_hungry = False

# You can evaluate an integer or float into a boolean using bool().
# An integer or float with a value of zero will evaluate to True.
# Any other number will evaluate to False.
print(bool(0))
print(bool(14))
print(bool(3.14))

# 4.a) Try evaluating other types to see what they will convert to.

# 5. Type and isinstance
# You can check the type of a variable using type().
print(type("I'm a string"))
print(type(99))

# You can evaluate if two things are the same type using isinstance().
print(isinstance(46, int))
print(isinstance(True, str))

# 6. None
# 'None' is special keyword that denotes no value. None has it's own type: 'NoneType'.
nothing_here = None
print(nothing_here)
print(type(nothing_here))

# 6.a) What do you think None will evaluate to using bool()? Try and see for yourself.

# 7. Datetime and time zone offset
import datetime

# 7.a) Print the current time using the datetime library.

# 7.b) Print the time in the above answer in the full date format (e.g. Sunday February 12 2023).

# 7.c) Using the above time, create the following statement using the current time variable
# 'Right now its HH:MM (AM/PM) on [Weekday], [Month] [Day], [Year]'
# E.g. 'Right now its 8:23 PM on Sunday, February 12, 2023'

# 7.d) Using the logic above, create the same statement but convert to the appropriate time zone in:
# - Vancouver
# - Paris
# - Tokyo
# E.g. 'Right now in Tokyo its 10:23 AM on Sunday, February 13, 2023'

# 7.e) Write a Python statement that will print the current amount of days till Christmas.
