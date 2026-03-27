#создаёт класс комплексных чисел и выполняет над ними математические операции
import math  # импортируем модуль math для математических операций

# Создаем класс Complex для работы с комплексными числами
class Complex(object):

    # Конструктор класса
    # real — действительная часть
    # imaginary — мнимая часть
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    # Переопределение оператора сложения "+"
    # позволяет складывать объекты класса Complex
    def __add__(self, no):
        # складываем действительные и мнимые части отдельно
        return Complex(self.real + no.real, self.imaginary + no.imaginary)
        
    # Переопределение оператора вычитания "-"
    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)
                
    # Переопределение оператора умножения "*"
    def __mul__(self, no):
        # Формула умножения комплексных чисел:
        # (a+bi)(c+di) = (ac - bd) + (ad + bc)i
        
        r = self.real * no.real - self.imaginary * no.imaginary
        i = self.real * no.imaginary + self.imaginary * no.real
        
        # возвращаем новое комплексное число
        return Complex(r, i)
        
    # Переопределение оператора деления "/"
    def __truediv__(self, no):
        
        # Формула деления:
        # (a+bi)/(c+di) = [(a+bi)(c-di)] / (c² + d²)
        
        # вычисляем знаменатель
        denom = no.real**2 + no.imaginary**2
        
        # проверяем деление на ноль
        if denom == 0:
            raise ValueError("Division by zero")
        
        # вычисляем действительную часть результата
        r = (self.real * no.real + self.imaginary * no.imaginary) / denom
        
        # вычисляем мнимую часть
        i = (self.imaginary * no.real - self.real * no.imaginary) / denom
        
        return Complex(r, i)
        
    # Метод вычисления модуля комплексного числа
    def mod(self):
        # |a+bi| = √(a² + b²)
        m = math.sqrt(self.real**2 + self.imaginary**2)
        
        # возвращаем как комплексное число (мнимая часть = 0)
        return Complex(m, 0)
        
    # Метод строкового представления числа
    # определяет как объект будет выводиться через print()
    def __str__(self):
        
        # если мнимая часть = 0
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
            
        # если действительная часть = 0
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
                
        # если мнимая часть положительная
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
            
        # если мнимая часть отрицательная
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
            
        return result


# Основная часть программы
if __name__ == '__main__':
    try:
        # считываем первую строку чисел
        c = map(float, input().split())
        
        # считываем вторую строку
        d = map(float, input().split())
        
        # создаем два комплексных числа
        x = Complex(*c)
        y = Complex(*d)
        
        # выполняем операции и выводим результаты
        print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
        
    except ValueError:
        pass