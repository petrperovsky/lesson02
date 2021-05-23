my_list = list(map(str, input('Введите элементы списка через пробел: ').split()))
n = 0
while n < len(my_list):
    my_list[n], my_list[n + 1] = my_list[n + 1], my_list[n]
    n += 2
    if n >= len(my_list) - 1:
        break
print(my_list)
