

num = int(input("Введите число: "))

def reverse_number(num):
    string = str(num)
    reversed_string = string[::-1]
    return int(reversed_string)

def is_polindrom(num):
    s = str(num)
    if s == s[::-1]:
        return True
    else:
        return False
    
reversed_num = reverse_number(num)

def reverse_number(n):
    reversed_str = str(n)[::-1]
    if reversed_str == str(n):
        print(f"{n} полидром")
    return int(reversed_str)

def process_numbers(numbers):
    reversed_numbers = []
    for num in numbers:
        reversed_numbers.append(reverse_number(num))
    return reversed_numbers

numbers = [123, 456, 789, 121, 343, 555]
result = process_numbers(numbers)
print("Reversed numbers:", result)

print("Перевернутое число:", reversed_num)

if is_polindrom(num):
    print('Число полиндром')
else:
    print("Число не полиндром")