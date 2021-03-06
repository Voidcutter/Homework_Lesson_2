#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''

for i in range(1, 6):
    print(i, ". ", 0, sep = "")

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
sum = 0

for i in range(0, 10):
    n = int(input("Enter a number: "))
    if n == 5:
        sum += 1
print("The amount of numbers 5 is:", sum)

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
sum = 0

for i in range(1, 101):
    sum += i
print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''

prod = 1

for i in range(1, 11):
    prod *= i
print(prod)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

integer_number = 2129

while integer_number > 0:
    print(integer_number % 10)
    integer_number = integer_number // 10

'''
Задача 6
Найти сумму цифр числа.
'''
sum = 0
integer_number = 21659

while integer_number > 0:
    sum += integer_number % 10
    integer_number = integer_number // 10
print(sum)

'''
Задача 7
Найти произведение цифр числа.
'''
sum = 1
integer_number = 53287

while integer_number > 0:
    sum *= integer_number % 10
    integer_number = integer_number // 10
print(sum)

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
integer_number = 213513
while integer_number > 0:
    if integer_number % 10 == 5:
        print('Yes')
        break
    integer_number = integer_number // 10
else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
n = 283413
a = 0

while n > 0:
    if a < n % 10:
        a = n % 10
    n = n // 10
print(a)

'''
Задача 10
Найти количество цифр 5 в числе
'''
sum = 0
n = 258513
while n > 0:
    if n % 10 == 5:
        sum += 1
    n = n // 10
print(sum)