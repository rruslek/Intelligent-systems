print('Выберите модель принятия коллективных решений:'
      '\n1-Относительного большинства'
      '\n2-Модель Борда'
      '\n0-Выход')
case = int(input())
print('Введите количество кандидатов:')
n = int(input())
print('Введите количество выборщиков:')
m = int(input())
points = [0 for i in range(n)]
matrix = [[0 for j in range(n)] for i in range(m)]

if case == 1:
    for i in range(m):
        print('ВЫБОРЩИК №' + str(i + 1))
        print('Введите № предпочитаемого кандидата  (от 1 до ' + str(n) + ')')
        k = int(input())
        points[k - 1] += 1
        matrix[i][k-1] = 1

if case == 2:
    for i in range(m):
        print('ВЫБОРЩИК №'+str(i + 1))
        for j in range(n):
            print('Введите место (от 1 до ' + str(n) + ') для кандидата №' + str(j + 1))
            k = int(input())
            points[j] += n - k
            matrix[i][j] = k

print('\nМАТРИЦА ГОЛОСОВАНИЯ:')
for i in range(m):
    print(matrix[i])

max = 0
winners = []

print('\nРЕЗУЛЬТАТ:')
for i in range(n):
    print('Кандидат №' + str(i + 1) + ' набрал ' + str(points[i]) + ' баллов')
    if points[i] >= max:
        if points[i] > max:
            winners.clear()
        max = points[i]
        winners.append(i)

if len(winners) == 1:
    print('\nПобедил кандидат №' + str(winners[0] + 1))
else:
    result = '\nКандидаты № '
    for winner in winners:
        result += str(winner + 1) + ' '
    result += 'набрали одинаковое количество баллов\nНужно проводить перевыборы!'
    print(result)
