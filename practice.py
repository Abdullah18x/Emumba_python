# patient_name = "John Smith"
# age = 20
# new_patient = True
# print(patient_name, age, new_patient)

# name = input("What is your name? ")
# print("Hello " + name)

# birth_year = input("Enter birth year: ")
# age = 2025 - int(birth_year)
# print(age)

# input_one = input("Enter first number: ")
# input_two = input("Enter second number: ")
# print("Sum is " + str(float(input_one) + float(input_two)))

# course = "Python for beginners"
# print(course)
# print(course.upper())
# print(course.lower())
# print(course.find("beginners"))
# print(course.replace("beginners", "absolute beginners"))
# print("Python" in course)

# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 ** 3)
# print(10 / 3)
# print(10 // 3)
# print(10 % 3)

# x = 3 > 2
# print(x)

# price = 25
# print(price > 5 and price < 10)
# print(not price > 5 or price < 10)

# temp = 30
# if temp > 30:
#     print("It's warm")
# elif temp > 20:
#     print("It's good")
# else:
#     print("It's cold")

# i = 1
# while i <= 10:
#     print(i * '*')
#     i = i + 1

# names = ["John", "Bob", "Mosh"]
# print(names)
# print(names[0])
# names[0] = "Jon"
# print(names)
# print(names[0:2])

# numbers = [1, 2, 3, 4, 5]
# numbers.append(6)
# print(numbers)
# numbers.insert(3, -1)
# print(numbers)
# numbers.remove(3)
# print(numbers)
# print(1 in numbers)
# print(len(numbers))

# numbers = [1, 2, 3, 4, 5]
# for i in numbers:
#     print(i)

# numbers = range(5)
# print(numbers)
# for i in numbers:
#     print(i)

# numbers = (1, 2, 3)
# print(numbers.count(3))

# number = 10
# if number > 5:
#     raise Exception(f"The number should not exceed 5. ({number=})")
# print(number)

# try:
#     number = 6
#     assert (number < 5), f"The number should not exceed 5. ({number=})"
# except AssertionError as error:
#     print(error)
# finally:
#     print("Finally")

# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise
    
# def sum(a, b):
#     return a + b

# print(sum(1, 2))

# fruits = { "apple", "banana", "cherry" }
# print(fruits)
# fruits.add("orange")
# print(fruits)
# fruits.remove("banana")
# print(fruits)

# fruits = { "apple": "red", "banana": "yellow", "cherry": "red" }
# print(fruits)
# print(fruits["apple"])

# f = open("text.txt")
# print(f.read())
# f.close()

with open("text.txt") as f:
    print(f.read())










