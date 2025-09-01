import csv
import re

# Fibonacci Series
number = int(input('Enter a number: '))
arr = []
a, b = 0, 1
while len(arr) < number:
    arr.append(a)
    a, b = b, a + b
print(arr)

# Word frequency
file_name = input('Enter file name: ')
with open(file_name, 'r', encoding='utf-8') as file:
    data = file.read()
    words = data.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    print(word_count)

# Data Validation
try:
    value = input('Enter Value: ')
    data_type = input('Enter Data Type: ').lower()
    if data_type == 'integer':
        try:
            int(value)
            print('Valid')
        except ValueError:
            print('Invalid')

    elif data_type == 'float':
        try:
            float(value)
            print('Valid')
        except ValueError:
            print('Invalid')

    elif data_type == 'string':
        print(isinstance(value, str))

    elif data_type == 'email':
        # Simple regex for email validation
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        print(re.match(pattern, value) is not None)
    else:
        raise ValueError(f'Unsupported data_type: {data_type}')
except Exception as e:
    print(e) 

# File handling
try:
    file_name = 'students.csv'
    with open(file_name, 'r', encoding='utf-8') as file:
        data = csv.reader(file, delimiter=',', quotechar='|')
        address = []
        for index, row in enumerate(data):
            address.append({'name': row[0], 'phone': row[1]})
            marks = row[2:]
            marks = [int(i) for i in marks]
            row_avg = str(sum(marks) / len(marks))
            row_with_avg = [row[0], row[1], row_avg]
            print(', '.join(row_with_avg))
        print(address)
        while True:
            question = input('Do you want to add a record (1) or search by name (2) or exit (3): ')
            if question == '1':
                name = input('Enter name: ')
                phone = input('Enter phone: ')
                address.append({'name': name, 'phone': phone})
            elif question == '2':
                name = input('Enter name: ')
                for i in address:
                    if i['name'] == name:
                        print(i)
            elif question == '3':
                break
except FileNotFoundError:
    print('File not found')
except Exception as e:
    print(e)

