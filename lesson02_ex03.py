season = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
month_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
while True:
    n = int(input('Введите номер месяца: '))
    if n not in month_list:
        print('Ошибка ввода')
        continue
    else:
        break
for key, value in season.items():
    if n in season[key]:
        print(f'{n}-й месяц - это {key}')
