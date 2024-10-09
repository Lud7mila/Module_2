first = int(input("Пожалуйста, введите первое целое число: "))
second = int(input("Пожалуйста, введите второе целое число: "))
third = int(input("Пожалуйста, введите третье целое число: "))

if first == second == third:
    print('\nКоличество одинаковых чисел среди введенных: 3')
elif first == second or first == third or second == third:
    print('\nКоличество одинаковых чисел среди введенных: 2')
else:
    print('\nКоличество одинаковых чисел среди введенных: 0')


