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



# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали 
# билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех 
# цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется 
# написать программу, которая проверяет счастливость билета.

# lucky_ticket = input('Введите шестизначный номер билета: ')
# if lucky_ticket.isdigit() and int(lucky_ticket) > 99999 and int(lucky_ticket) < 1000000:
#     if int(lucky_ticket[0]) + int(lucky_ticket[1]) + int(lucky_ticket[2]) == int(lucky_ticket[3]) + int(lucky_ticket[4]) + int(lucky_ticket[5]):
#         print('Поздравляю! Ваш билет счастливый!')
#     else:
#         print('Увы, билет несчастливый. Вам повезет обязательно в другой раз.')
# elif lucky_ticket.isdigit() and int(lucky_ticket) < 100000 or lucky_ticket.isdigit() and int(lucky_ticket) > 999999:
#     print('Вероятно вы ввели не тот номер')
# else:
#     print('Вы уверены, что вы ввели число?')

    

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается 
# сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# n = int(input('Введите количество долек шоколадки по вертикали: '))
# m = int(input('Введите количество долек шоколадки по горизонтали: '))
# k = int(input('Сколько вы хотите отломить долек: '))
# if k < m * n and k % m == 0 or k < m * n and k % n == 0:
#     print('Да, вы можете отделить столько долек')
# else:
#      print('Нет, вы не можете отделить столько долек')
