
goods, number = [], 1

while input('Хотите добавить товар и его характеристики? (да / нет): '.lower()) == 'да':
    title = input('введите название товара: ')
    price = int(input('введите цену товара: '))
    amount = int(input('введите количество товара: '))
    unit = input('введите единицу измерения товара: ')
    goods.append((number, {'название': title, 'цена': price, 'количество': amount, 'ед.': unit}))
    number += 1
print(goods)

analytics = {'название': [], 'цена': [], 'количество': [], 'ед.': set()}
for key, feature in goods:
    analytics['название'].append(feature['название'])
    analytics['цена'].append(feature['цена'])
    analytics['количество'].append(feature['количество'])
    analytics['ед.'].add(feature['ед.'])

print(analytics)




