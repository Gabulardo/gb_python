# list
month = int(input('Введите любой месяц года ввиде целого числа от 1 до 12: '))
list_year = ['Зима', 'Весна', 'Лето', 'Осень']
if month == 1 or month == 2 or month == 12:
    print('Вы ввели месяц соответствующий времени года - ', list_year[0])
elif month == 3 or month == 4 or month == 5:
    print('Вы ввели месяц соответствующий времени года - ', list_year[1])
elif month == 6 or month == 7 or month == 8:
    print('Вы ввели месяц соответствующий времени года - ', list_year[2])
elif month == 9 or month == 10 or month == 11:
    print('Вы ввели месяц соответствующий времени года - ', list_year[3])



