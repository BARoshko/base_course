
#Конструкция if

if 1:
    print('hello 1')

a = 3
if a > 1:
    print(f'hello {a}')

b = 5
if b == 5:  # Операция сравнения
    print(f'hello {b}')

#Конструкция if – else

a = 3
if a > 4:
    print('hello 4')
else:
    print(f'hello {a}')

#Конструкция if – elif – else

a = 3
if a > 5:
    print('hello 5')
elif a < 2:
    print('hello 2')
else:
    print('Tupo hello')

#Логические операции
a = 3
b = 4
c = 5

if a > 4 and b == 2:  # and - операция логического "И"
    print('Good')
elif b > 3 or c == 5:  # or - операция логического "ИЛИ"
    print('Best')
else:
    print('Bad')

#Тренировка
a = 3
b = 5
c = -1

if a > 3 or c == 0:
    print('Good')
elif a <= 3 and b != 5:
    print('Best')
else:
    print('Bad')

if a >= 3 or b == 0:
    print('Good')
elif c == -1 or b > 4:
    print('Best')
else:
    print('Bad')

if ((a == 3 and c > 0) or (b == 5 and c < 0)) and c == -1:
    print('Good')
else:
    print('Bed')