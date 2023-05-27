"""
Исходные данные:

    свои ФИО, число, месяц, год рождения в виде кортежа;
    предметы в школьном аттестате (не меньше 14), как словарь из названия и оценки (можно мокать);
    имена (только) ближайших (до двоюродных включительно) родственников в списке и их год рождения через пробел (в одной строке);
    имя, которое вы бы дали своей домашней пушистой киве (строка).
"""

import datetime  # для 7 задания(дни от ДР)

from collections import deque  # для 8 задания(очередь FIFO)


tuple = ("Лудин Дмитрий Сергеевич", 8, 6, 2003,) # ФИО, число, месяц, год рождения в виде кортежа


dict = { "Алгебра" : 3 ,"Биология" : 4 ,"Всеобщая история" : 4 ,"География" : 5 , "Геометрия" : 4 , "Иностранный язык(английский)" : 4 ,
         "информатика" : 5 , "История России" : 4 , "Литература" : 4 , "ОБЖ" : 5 , "Обществознание" : 5 , "Русский язык" : 4 , "Физика" : 4 ,
         "Физическая культура" : 5 , "Химия" : 5 ,     } # предметы в школьном аттестате


list1 = ["Андрей" , 'Владимир' , 'Анна' , 'Сергей' , 'Федор' , 'Нина' , 'Николай' , 'Антон' , 'Арсений' , 'Дмитрий(я)' ]
# имена ближайших родственников 


name_kiva = "Брат" # имя моей пушистой кивы(краб Йети)


# 1  ---------------------------------
print(1)

print("Cредняя оценка аттестата = " , sum( dict.values()) / len(dict.values()))   # вывести среднюю оценку в аттестате ( сумма оценок / количество ключей)
print()


# 2  ---------------------------------
print(2)

print("Уникальные имена:" , list(set(list1)))      # вывести уникальные имена среди своих родственников (включая свое) (сортировка словаря методом list)
print()


# 3  ---------------------------------
print(3)

total = 0
for i in dict.keys():                              #Сумма всех знаков в названии предметов(обычный цикл for )
    total += len(i)
print("Сумма всех знаков в названии предметов =" , total)
print()


# 4  ---------------------------------
print(4)

vse_bukvi = ""     
for i in list(dict):                              # Уникальные буквы в названиях предметов
    vse_bukvi += i                              
print("Уникальные буквы в названиях предметов:" , set(list(vse_bukvi))) 
print()

# 5  ---------------------------------
print(5)

print("Имя пушистой кивы в обычном виде:" )
print(name_kiva)
bin_result = ''.join(format(ord(x), '08b') for x in name_kiva)
print("Имя пушистой кивы в бинарном виде:")                # Источник: https://pythonpip.ru/examples/stroka-v-dvoichnyy-kod-v-python
print(bin_result)
print()


# 6  ---------------------------------
print(6)

list1.sort(reverse=True)                # отсортированный по алфавиту (в обратном порядке) список родственников методом sort 
print("Oтсортированный по алфавиту (в обратном порядке) список родственников", list1)   #передавая обратный аргумент как True
print()


# 7  ---------------------------------
print(7)

# Количество дней от моего ДР до сегодня

today = datetime.datetime.now()                # сегодня в формате год, месяц, день, час, минуты
bday = datetime.datetime(2003 , 6 , 8 , 0 , 2) # год, месяц, день, час, минуты

time_diff = today - bday                       # полная разница по дням, часам и минутам
tdiff = time_diff.days                         # преобразуем в просто дни
print("Количество дней от моего ДР до сегодня", tdiff)     # Источник: https://habr.com/ru/company/ruvds/blog/648237/
print()


# 8  ---------------------------------
print(8)


n5 = int(input("Введите количество элементов в списке FIFO:"))
dq = []             # очередь FIFO

for i in range(1, n5 + 1):
    element_fifo = input("Введите элемент списка №"+str(i) +" ")
    dq.append(element_fifo)    # цикл на добавление в очередь элементов
    
print("Вы ввели очередь ", dq)


stop_slovo = input("Введите команду остановки: ")

slovo = ""

while True:
    index = int(input("Введите индекс элемента: "))    # индекс элемента , т.е. там где нужно добавлять элемент
    slovo = input("Введите элемент: ")                 # сам элемент , который добавлять надо
    if slovo == stop_slovo:
        break
    dq.insert(index , slovo)                           # добавление в очередь методом .insert()
    
print("В итоге FIFO очередь: " , dq)                   # Источник: https://proproprogs.ru/structure_data/std-ochered-collectionsdeque-na-python 
print()


# 9 ---------------------------------
print(9)

name_boss = ['Tenoch', 'Acamapochtli', 'Huitzilihitl', 'Chimalpopoca', 'Xihuitl Temoc',
            'Itzcoatl', 'Moctezuma I', 'Atotoztli', 'Axayacatl', 'Tizoc', 'Ahuitzotl',
            'Moctezuma II', 'Cuitlahuac', 'Cuauhtrmoc', 'Tlacotzin', 'Motelchiuhtzin',
            'Xochiquentzin', 'Huanitzin', 'Tehuetzquititzin', 'Cecetzin', 'Cipac']

number = (8 + 6 ** 2 + 2003) % 21 + 1  # индекс в списке name_boss 
print("Номер из списка правителей: ", number)

list1.sort()       # сортировка списка родственников
print(list1)
index9 = int(input("Введите индекс из списка моих родсвенников: "))

list1[index9] = name_boss[number]    # замена имени родственника на имя ацтекского правителя
print("Список родственников с замененным именем родственника с индексом ",index9 , list1)
print()


# 10 --------------------------------
print(10)






















