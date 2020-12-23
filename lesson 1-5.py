proceeds = int(input('Укажите выручку вашей фирмы, в руб.: '))
costs = int(input('Укажите издержки вашей фирмы, в руб.: '))
profit = proceeds - costs
profitability = profit / proceeds
if proceeds > costs:
    print('У Вас прибыльная фирма. Ваша прибыль составляет, в руб.:', profit,)
    print(f'Рентабельность Вашей фирмы составляет: {profitability:.0%}')
    numbers = int(input('Назовите численность вашей фирмы, чел.: '))
    average = profit / numbers
    print(f'Прибыль Вашей фирмы в расчете на одного сотрудника составляет, руб.: {average:.0f}')
else:
    print('Вы ведете убыточную деятельнось!')

