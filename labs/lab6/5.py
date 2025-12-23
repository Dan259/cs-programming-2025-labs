a = list(input('Введите текст без знаков препинания:').lower())
    
#Удаление пробелов
for i in range(a.count(' ')):
    a.remove(' ')
b = a[::-1]

#Проверка на палиндром
if a == b:
    print("Да")
else:
    print("Нет")