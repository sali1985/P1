#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def bar(name, surname, year, city, email, number):
    print(f'name - {name}, surname - {surname}, year - {year}, city - {city}, email - {email}, number - {number}')

bar(name = 'Sava', surname = 'Savushkin', year = '1985', city = 'Moscow', email= 'gek@listt.ru',
        number = '+78569869')