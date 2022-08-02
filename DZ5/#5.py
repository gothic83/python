# 1- Напишите программу, удаляющую из текста все слова, содержащие "хер"
# text=('херувимы в херосиме покрасили забор')

# def filter_text(text):
#     text=text.split(' ')
#     text_new=lambda word: 'хер' not in word
#     return '  '.join(list(filter(text_new,text)))
# print(filter_text(text))


# #2 Мой уровень програмирования оооооооочень далёк от написания игр... я не умный бот.
# даже посмотрев на решения поставленной задачи и нифига не понял.

# #3
# from functools import reduce

# def create_list():
#     languages =('c#', 'pyhton','java','basic','pascal')
#     numbers =list(range(1,len(languages)+1))
#     lst=enumerate([word.upper() for word in languages])
#     return list(lst)
# print(create_list())

# def filter_sum(lst):
#     result=[]
#     sum=0
#     for numbers,languages in lst:
#         point=reduce(lambda a,b: a+b, [ord(char) for char in languages])
#         if point % numbers==0:
#             sum+=point
#             result.append((point,languages))
#     del lst
#     return sum, result
# print(filter_sum(create_list))
# Вроде бы правильно списал, а что-то всё равно не работает. часа 2 сидел... надоело

# 4- Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления 
# данных.Входные и выходные данные хранятся в отдельных текстовых файлах

#Нет желания самостоятельно искать что за слово такое RLE. Думаю это мне не пригодится в жизни. 
# Это мы не проходили..