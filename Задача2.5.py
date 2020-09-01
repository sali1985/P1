
chislo = int(input('Введите номер рейтинга '))
my_list = [6, 4, 3, 3, 1]
my_list.extend([chislo])
my_list = sorted(my_list, reverse = True)
print(my_list)