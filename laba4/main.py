import array

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

if case == 1:
    for i in range(m):
        print('ВЫБОРЩИК №' + str(i + 1))
        print('Введите № предпочитаемого кандидата  (от 1 до ' + str(n) + ')')
        points[int(input()) - 1] += 1

if case == 2:
    for i in range(m):
        print('ВЫБОРЩИК №'+str(i + 1))
        for j in range(n):
            print('Введите свою оценку (от 1 до ' + str(n) + ')  кандидату №' + str(j + 1))
            points[j] += n - int(input())

max = 0
winners = []
for i in range(n):
    print('\nКандидат №' + str(i + 1) + ' набрал ' + str(points[i]) + ' баллов')
    if points[i] >= max:
        max = points[i]
        winners.append(i)
if len(winners) == 1:
    print('\nРЕЗУЛЬТАТ:\nПобедил кандидат №' + str(winners[0] + 1))
else:
    result = '\nРЕЗУЛЬТАТ:\nКандидаты № '
    for winner in winners:
        result += str(winner + 1) + ' '
    result += 'набрали одинаковое количество баллов\nНужно проводить перевыборы!'
    print(result)
