formuls = input('Введите формулы:').split(',')
kol = len(folmuls)
if kol == 2:
    if formuls[0] in formuls[1][:formuls[1].find('<')]:
        if '<=' in formuls[1]:
            print('Заключение:')
            print(formuls[1].replace(formuls[0] + ' <='))
        else:
            print('Нет modus ponens')