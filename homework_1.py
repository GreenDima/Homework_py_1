## Задача 2: Найдите сумму цифр трехзначного числа.

# num = int(input('Введите трехзначное число: '))
# sum = 0
# if num > 99 and num < 1000:
#     while num > 0:
#         sum += num % 10
#         num //= 10
#     print(f'Сумма цифр введенного числа: {sum}')
# else:
#      print('Вы ввели не трехзначное чиcло!')

## Решил еще таким способом

# num = input('Введите трехзначное число: ')
# if num.isdigit() == True and int(num) > 99 and int(num) < 1000:
#     print(f'Сумма цифр введенного числа: {int(num[1]) + int(num[0]) + int(num[2])}')
# else:
#     print('Вы ввели либо не число или это число не трехзначное!')



# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое 
# количество журавликов,  а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# sum_cranes = int(input('Введите количество журавликов, которых сделали дети: '))
# if sum_cranes % 6 == 0 and sum_cranes > 0:
#     print(f'Катя сделала {(sum_cranes // 6) * 4} шт.')
#     print(f'Петя и Сережа сделали по {sum_cranes // 6} шт. каждый.')
# else:
#     print(f'Катя сделала {(sum_cranes // 6) * 4} шт.')
#     print(f'Петя и Сережа сделали по {sum_cranes // 6} шт. каждый.')
#     print('Недостающие журавлики в разработке.')



