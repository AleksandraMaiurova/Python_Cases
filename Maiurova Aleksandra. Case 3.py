# Запросим данные у пользователя
text = input('Введите код: ')
# Создадим словарь моделей игрушки
model = {
    'C':'Машинка',
    'RT': 'Кролик',
    'BR': 'Медведь',
    'LMT': 'Паровоз'
}
# Создадим словарь цветов игрушки
color = {
    '1': 'Красный',
    '2': 'Чёрный',
    '3': 'Белый',
    '4': 'Зелёный',
    '5': 'Синий',
    '6': 'Фиолетовый'
}

text_color = color[text[-1]]
text_model = model[text[:-1]]

print(text_color, text_model)