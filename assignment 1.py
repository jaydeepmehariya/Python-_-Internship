#  Question-1
print("Hello, World!")

# Question-2 
name = "Jaydeep"
age = 26
hobby = "Singing"
print(f"name : {name}")
print(f"age : {age}")
print(f"hobby : {hobby}")

# Question-3
print("Hello, World!") #this  will print "hello world"
name = "Jaydeep"     #Assigning String to a variable (name)
age = 26             #Assigning integer to a variable (age)  

# Question-4
number = int(input("Enter an integer: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Question-5
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Question-6
for number in range(1, 11):
    print(number)

# Question-7
number = int(input("Enter an integer: "))
i = 1       
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1

# Question-8
for num in range(1,11):
    if num % 3 == 0:
        continue
    print(num)

# Question-9
for num in range(1, 11):
    if num > 5:
        break
    print(num)

# Question-10
def greet(name):
    print(f"Hello, {name}!")

greet("Jaydeep")

# Question-11
def add(x,y):
    return x + y
result = add(1,11) 
print(result)