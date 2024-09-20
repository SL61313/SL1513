char = input("Введите символ: ")

a = 1

while a <= 5:
    print(char * a)
    a = a+1


months = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декабрь'
}

while True:
    month_input = input('Введите номер месяца (от 1 до 12): ')

    if month_input.isdigit():
        month_id = int(month_input)
        if 1 <= month_id <= 12:
            print(months[month_id])
            print('Поздравляю, у тебя получилось')
            break
        else:
            print("Нет такого месяца, пробуй снова")
    else:
        print("Вводи целые положительные числа,пробуй снова")

