# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с 
# помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# a = int(input("Введите число: "))
# b = int(input("Введите степень числа: "))

# def power(a,b):
#     if b == 1:
#         return a
#     else:
#         c = a * power(a, b-1)
#         return c
# print("Результат:", power(a, b))


# Дана строка (возможно, пустая), состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28 
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения: Если символ встречается 1 раз, он остается без изменений; Если символ повторяется более 1 раза,
# к нему добавляется количество повторений.



# def func(inStr):
#     outStr = str()
#     count = 1
#     for i in range(len(inStr)-1):
#         if inStr[i] == inStr[i+1]:
#             count +=1
#         else:
#             outStr += inStr[i]
#             if count > 1:
#                 outStr += str(count)
#                 count = 1
#     if inStr[-1] in inStr:
#         outStr += inStr[-1]
#     if count > 1:
#         outStr += str(count)
#     return outStr

# s = "AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB"
# print(func(s))