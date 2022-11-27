# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# print('Enter number:')
# a = float(input())
# print(a)
# result = 0
# while (a % 1) != 0:
#     a = a * 10
# print(a)
# b = int(a)
# print(b)
# while(b * 10 // 10) != 0:
#         c = b % 10
#         result = result + c
#         b = b // 10
# print(f'Elements sum = {result}')            

# этот код все значения считает верно, например 0.55 => cумма 10, 0.63=>сумма9, 6782=>сумма23,
# 0.142=>сумма7. НО когда я подставляю 0.56 или 0.14 или 0.23 он выдает неверную сумму, почему? Хотя числа 0.55, 0.13, 0.22 и все
# остальны он считает верно, но так же есть числа (типо как исключения, не знаю) которые он считает не верно из за преобразования в инт
# хотя по условию, чем отличается перевод числа 0.55 и 0.56 я не понимаю. Почему для 0.55 и другие считает верно а для 0.56 и 0.14 нет?
# Через десимал при этом все рабоет и для 0.56 и 0.14 но почему если они флоат, именно эти значения не хочет считать?

# from decimal import Decimal
# print('Enter number:')
# a = abs(Decimal(input()))
# result = 0
# while (a % 1) != 0:
#     a = a * 10
# print(a)
# b = int(a)
# print(b)
# while(b * 10 // 10) != 0:
#         c = b % 10
#         result = result + c
#         b = b // 10
# print(f'Elements sum = {result}') 



# Задайте список из n чисел последовательности (1 + 1/n)^n. Вывестив консоль сам список и сумму его элементов.
# print('How many elements in list?:')
# a = int(input())
# list = []
# for i in range(1, a + 1):
#     list.append(round(((1 + 1/i)**i), 2))
# print(list)
# sum = 0
# for i in range (len(list)):
#     sum = sum + list[i]
# print(f'Sum for elements in this list = {sum}')


# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод
# print('How many digits in list?:')
# a = int(input())
# list = []
# for i in range(1, a + 1):
#     print('Enter element:')
#     b = int(input())
#     list.append(b)
# print(list)
# def Change(array):
#     i = 0
#     while(i < len(array) / 2):
#         x = array[i]
#         array[i] = array[len(array) - 1 - i]
#         array[len(array) - 1 - i] = x
#         i = i + 1
# Change(list)
# print(f'Sorted list = {list}')
