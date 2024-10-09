my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

index = 0
list_len = len(my_list)

while index < list_len:
    if my_list[index] > 0:
        print(my_list[index])
    elif my_list[index] < 0:
        break
    index += 1
