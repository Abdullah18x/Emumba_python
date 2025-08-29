# Calculator
def calculator():
    try:
        num_1 = input('Enter first number: ')
        num_2 = input('Enter second number: ')
        operator = input('Enter operator: ')

        if operator == '+':
            print(int(num_1) + int(num_2))
        elif operator == '-':
            print(int(num_1) - int(num_2))
        elif operator == '*':
            print(int(num_1) * int(num_2))
        elif operator == '/':
            print(int(num_1) / int(num_2))
        else:
            print('Invalid operator')
    except ValueError:
        print('Invalid input')
    except ZeroDivisionError:
        print('Cannot divide by zero')
    except Exception as e:
        print(e)


# Temperature Converter
def temperature_converter():
    try:
        temp = input('Enter temperature: ')
        unit = input('Enter unit Celsius (C) or Fahrenheit (F): ')
        if unit == 'C':
            print((int(temp) * 9/5) + 32)
        elif unit == 'F':
            print((int(temp) - 32) * 5/9)
        else:
            print('Invalid unit')
    except ValueError:
        print('Invalid input')
    except Exception as e:
        print(e)

# Vowel Counter
def vowel_counter():
    try:
        word = input('Enter a word: ')
        count = 0
        for char in word:
            if char in 'aeiou':
                count += 1
        print(count)
    except ValueError:
        print('Invalid input')
    except Exception as e:
        print(e)

# List Operations
def list_operations():
    try:
        list = input('Enter a list of numbers separated by commas: ')
        list = list.split(',')
        print(list)
        # Convert list to int
        i = 0
        while i < len(list):
            list[i] = int(list[i])
            i += 1
        # Actions on list
        print('Sum of list = ' + str(sum(list)))
        print('Average of list = ' + str(sum(list)/len(list)))
        print('Max of list = ' + str(max(list)))
        print('Reverse of list = ' + str(list[::-1]))
    except ValueError:
        print('Invalid input')
    except Exception as e:
        print(e)

while True:
    print("1. Calculator")
    print("2. Temperature Converter")
    print("3. Vowel Counter")
    print("4. List Operations")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        calculator()
    elif choice == '2':
        temperature_converter()
    elif choice == '3':
        vowel_counter()
    elif choice == '4':
        list_operations()
    elif choice == '5':
        break
    else:
        print("Invalid choice")
