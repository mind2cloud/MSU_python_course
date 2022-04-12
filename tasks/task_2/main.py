import cmath as cm
def input_number(number):
    def mult(mult):
        number * mult
    def pow(pow):
        number ** pow
    def div(a):
        number / a
    def sin(a):
        cm.sin(number * a)
f = input_number(5)
print(input_number(5))

#Функция либо умножает, либо возводит в степень с разными аргументами
#Можно использовать словари и пр.
