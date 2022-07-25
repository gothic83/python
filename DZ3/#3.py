# 1 - Задайте список из нескольких чисел. Напишите программу,
#  которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# from random import randint
# n=int(input('Введите число элементов в списке: '))
# min=int(input('Введите минимальное число в списке: '))
# max=int(input('Введите максимальное число в списке: '))
# def get_lst(n, min, max):
#     return [randint(min, max) for i in range(n)]
# def sum_odd_position(new_list):
#     return sum(new_list[1::2])
# new_list = get_lst(n,min,max)
# print(new_list)
# print(sum_odd_position(new_list))

# 2 - Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# import math
# from random import randint
# n=int(input('Введите число элементов в списке: '))
# min=0
# max=int(input('Введите максимальное число в списке: '))
# def get_lst(n, min, max):
#     return [randint(min, max) for i in range(n)]
# def multiple(new_list):
#     return [new_list[i] * new_list[-i - 1] for i in range(math.ceil(len(new_list)/2))]
# new_list=get_lst(n, min, max)
# print('Cписок ->',new_list)
# print('Произведение пар чисел списка ->',multiple(new_list))

# 3 - Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.

# from random import uniform
# n=int(input('Введите число элементов в списке: '))
# a=0
# b=int(input('Введите максимальное число в списке: '))
# def get_nums (n, a, b):
#     return [round(uniform(a,b), 2) for i in range(n)]
# def find_diff(numbers):
#     nums = [round(i - int(i), 2) for i in (numbers)]
#     return max(nums) - min(nums)
# numbers = get_nums(n, a, b)
# print (numbers)
# print('Разница между максимальным и минимальным значением дробной части элементов =', find_diff(numbers))

# 4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# n = int(input('Введите число: '))
# def dec_to_bin(n):
#     bin_num = []
#     while n > 0:
#         bin_num.insert(0, n % 2)
#         n = n // 2
#     return bin_num
# print('Число "', n , '" в двоичной системе =' , dec_to_bin(n))

# 5 - Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
n = int(input('Введите число: '))
def fibonacci(n):
    fib = []
    a, b = 1, 1
    for i in range(n):
        fib.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n+1):
        fib.insert(0, a)
        a, b = b, a - b
    return fib
fib = fibonacci(n)
print(fibonacci(n))

