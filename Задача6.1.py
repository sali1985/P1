# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
# — на ваше усмотрение. Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

class TrafficLight:
    _color1 = 'Red'
    _color2 = 'Yellow'
    _color3 = 'Green'



import time
my_lights = TrafficLight()
print(my_lights._color1)
time.sleep(7)
print(my_lights._color2)
time.sleep(2)
print(my_lights._color3)
time.sleep(3)
