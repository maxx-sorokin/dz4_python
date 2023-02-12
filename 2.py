# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

number = int(input('Введите число: '))
prime_number_list = list()
while number != 1:
    if number % 2 == 0:
        prime_number_list.append(2)
        number //= 2
    elif number % 3 == 0:
        prime_number_list.append(3)
        number //= 3
    elif number % 5 == 0:
        prime_number_list.append(5)
        number //= 5
    elif number % 7 == 0:
        prime_number_list.append(7)
        number //= 7
    else:
        prime_number_list.append(number)
        number //= number

print(prime_number_list)
