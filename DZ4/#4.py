# 1- Вычислить число c заданной точностью d. Число Пи не просто обрезать с math.pi, а вычислить, используя 
# формулы: Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.

#Даже если я и спишу, то всё равно не пойму что это за ерунда и чего от меня требуется, поэтому пропущу это...


# 2- Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности. 

# lst=[1,2,3,4,8,1,2,3,4,1,2,3,4,5]

# def sort(sub1):
#     a=[]
#     for i in lst:
#         if i not in a:
#             a.append(i)
#     return a
# print(sort(lst))

# 3- Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# def lst(n):
#     lst1=[]
#     i=2
#     while n !=1:
#         if n%i ==0:
#             lst1.append(i)
#             n=n//i
#         else:
#             i=i+1
#     return lst1
# print(set(lst(12)))


 # 4 - В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# В файле содержится, например:
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893

file = open('text.txt',"w",encoding='utf-8')
file.write('Мама сшила м0не штаны и7з бере9зовой кор45ы 893')
file.close
file = open('text.txt',"r",encoding='utf-8')
data=file.read().split()
lst=[]
for words in data:
    if words.isalpha():
        lst.append(words)
file.close()
print(' '.join(lst))