# 1- Определить, присутствует ли в заданном списке строк, некоторое число

# lst=['ма0ма', 'па9098па' ,'и' ,'евламп890ий', 'говорили', 'на', 'ара09бском', 'языке','долго225']
# def num(lst,number):
#     return list(filter(lambda word: str(number) in word,lst))
# print(num(lst,0))


# #2- Найти сумму чисел списка стоящих на нечетной позиции
# import math
# n = int(input('Введите число элементов массива: '))
# def sums(n:int):
#     num=list(range(1,n+1))
#     print(num)
#     num=list(filter(lambda element: num.index(element)%2,num))
#     print(num)
#     return sum(num)
# print('Сумма чётных элементов массива' ,sums(n))

# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)
# import math
# coordinat= [2,6,7,8]
# def distanciya(text : int):
#     x1,y1,x2,y2=list(map(int,text))
#     return ((x2-x1)**2+(y2-y1)**2)**0.5
# print('Расстояние между точками = ' ,round(distanciya(coordinat),3))

# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# при других несуществующих данных ошибка какая то вылазит.IndexError: list index out of range я по 
# английски не понимаю.

# lst=["йцу", "фыв","йцукен", "ячс", "цук",  "йцу"]
# num='цук'
# def element(lst:str, num:int):
#         return [i for i,element in enumerate(lst) if num in element][1] if len(lst)>=2 else 0
# print(element(lst,num)

#5-Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.

# import math
# n=int(input('Введите число элементов списка: '))
# lst=[x for x in range(1,n)]
# print(lst)
# def mult(lst):
#     return [lst[i]*lst[-i-1] for i in range(math.ceil(len(lst)/2))]
# print(mult(lst))

# 6-Сформировать список из  N членов последовательности.

n=int(input('Введите число членов последовательности: '))
def sequence(n):
    return [-3 **i for i in range(1, n+1)]
print(sequence(n))       # не так как в примере получается почему то..
seq = list(lambda n: [-3 **i for i in range(1, n+1)])
print(seq)   # ничего не печатает... ошибка какая то

