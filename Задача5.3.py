

with open('workers.txt', 'r', encoding= 'utf-8') as my_file:
    workers = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           poor.append(i[0])
        workers.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, workers)) / len(workers)}')