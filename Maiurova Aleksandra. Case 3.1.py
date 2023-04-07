# Чек покупателя
receipts = [{'Хлеб': 65, 'Конфеты': 345, 'Яблоки': 65, 'Чай': 76, 'Картофель': 48}, {'Хлеб': 55, 'Вода': 80, 'Рыба': 351,
'Кофе': 292, 'Яблоки': 97}, {'Чай': 118, 'Картофель': 55, 'Кофе': 324, 'Рыба': 359, 'Конфеты': 240, 'Мясо': 298}, {'Мясо':
352, 'Картофель': 54, 'Конфеты': 305, 'Кофе': 318, 'Шоколад': 73}, {'Хлеб': 48, 'Яблоки': 104, 'Мясо': 454, 'Молоко': 80,
'Шоколад': 96, 'Картофель': 33}]
sweets = ['Конфеты', 'Шоколад']
saved_money = 0
saved_money+=receipts[0].get(sweets[0],0)
saved_money+=receipts[0].get(sweets[1],0)
saved_money+=receipts[1].get(sweets[0],0)
saved_money+=receipts[1].get(sweets[1],0)
saved_money+=receipts[2].get(sweets[0],0)
saved_money+=receipts[2].get(sweets[1],0)
saved_money+=receipts[3].get(sweets[0],0)
saved_money+=receipts[3].get(sweets[1],0)
saved_money+=receipts[4].get(sweets[0],0)
saved_money+=receipts[4].get(sweets[1],0)
print(f'Дядя Вова сможет сэкономить в следующем месяце {saved_money} рубл(я/ей).')