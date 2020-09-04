#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def dva_chisla():

    try:
       chislo1 = int(input('Введите первое число '))
       chislo2 = int(input('Введите второе число '))
       name = chislo1 / chislo2
    except ZeroDivisionError:
        return 'Вы не можете вводить 0  '

    return name
chislo3 = dva_chisla()
print(chislo3)

