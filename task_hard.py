
number_n = int(input('Введите число из первой вставки, для которого нужно подобрать пароль (от 3 до 20): '))

password = ''
for number_1 in range(1, number_n // 2 + 1):
    for number_2 in range(number_1 + 1, number_n - number_1 + 1):
        if number_n % (number_1 + number_2) == 0:
            password += str(number_1) + str(number_2)

print('\nВ результате получился такой пароль:', password)