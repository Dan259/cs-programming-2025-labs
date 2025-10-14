# def num1():
#     a = int(input('Введите температуру:'))
#     if a < 20:
#         print('Кондиционер включен')
#     else:
#         print('Кондиционер выключен')

# def num2():
#     a = int(input("Введите месяц:"))
#     if a > 0 and a < 3 or a == 12:
#         print('Winter')
#     elif a > 2 and a < 6:
#         print('Spring')
#     elif a > 5 and a < 9:
#         print('Summer')
#     elif a > 8 and a < 12:
#         print('Autumn')

# def num3():
#     a = input('Введите возраст:')
#     b = 0
#     c = False
#     d = []
#     for i in range(1,100):
#         d.append(str(i))
    
#     if a in d:
#         c = True

#     if c == True:
#         a = int(a)
#         if a > 1 and a < 23:
#             if a == 2:
#                 b = 21
#                 print(b)
#             else:
#                 b = 21 + ((a-2) * 4)
#                 print(b)
#         else:
#             print('Error, age cannot be smaller than 1 and bigger than 22')
#     else:
#         print('Error, incorrect type of input')

# def num4():
#     a = input('Enter number:')
#     b = 0
#     for i in range(len(a)-1):
#         b += int(a[i])

#     if int(a[len(a)-1]) // 2 == 0 and b // 3 == 0:
#         print('Число кратно 6')

a = '10'
print(a)
