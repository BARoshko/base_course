""" Квадратное уравнение """


print("Решение квадратного уравнения вида ax^2+bx+c=0\nВведите:")

try:
    a = float(input('первый член a='))
    b = float(input('второй член b='))
    c = float(input('третий член c='))
except ValueError:
    print('Ошибка: введите корректное число')
except KeyboardInterrupt:
    print('Программа прервана пользователем')
except Exception as e:
    print('Неизвестная ошибка')

else:
    if a == 0:
        try:
            x = float(-c / b)
        except ZeroDivisionError:
            print('На 0 делить нельзя (ваш член "b" не должен равняться нулю)')
        else:
            print('\nРезультат')
            print('Корень уравнения равен', round(x, 5))
    else:
        x = 0
        x1 = 0
        x2 = 0
        D = float(b**2-4*a*c)
        if D < 0:
            print('\nРезультат')
            print('Нет рациональных корней')
        elif D == 0:
            try:
                x = float(-b / (2 * a))
            except ZeroDivisionError:
                print('На 0 делить нельзя (ваш член "а" не должен равняться нулю)')
            else:
                
                print('\nРезультат')
                print('Корень уравнения равен', round(x, 5))
        elif D > 0:
            try:
                x1 = float((-b+D**0.5) / (2 * a))
                x2 = float((-b-D ** 0.5) / (2 * a))
            except ZeroDivisionError:
                print('На 0 делить нельзя (ваш член "а" не должен равняться нулю)')
            else:
                print('\nРезультат')
                print('Первый корень уравнения равен', round(x1, 5))
                print('Второй корень уравнения равен', round(x2, 5))