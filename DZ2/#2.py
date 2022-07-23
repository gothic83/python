
# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# n=int(input('Введите число: '))
# def sum(n):
#     result = 0
#     while n > 0:
#         result += n % 10
#         n //= 10
#     return result
# print(sum(n))

# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# def mult(n):
#     if n == 1:
#         return 1
#     else:
#         return n * mult(n - 1)
# number=int(input('Введите число: '))
# list = []
# for i in range(1, number + 1):
#     list.append(mult(i))

# print(f"Произведения чисел от 1 до {number}:  {list}")

# 3. Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

# n = int(input('Введите число: ')) 
# def squerence(n):
#     return {round((1 + 1 / x)**x, 8) for x in range (1, n + 1)}
# print(squerence(n))
# print('Сумма чисел в списке = ',sum(squerence(n)))



#4 не в курсе что это такое...  биты, библиотека time (миллисекунды или наносекунды) - 
# для задания случайности