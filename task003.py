# 3 (необязательное). Напишите программу, которая принимает
# на стандартный вход список игр футбольных команд с результатом матча
# и выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
#
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
#
# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков
#
# Конкретный пример ввода-вывода приведён ниже.
#
# Порядок вывода команд произвольный.
#
# Sample Input:
#
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:
#
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6


def data_input():
    game_results = []
    game_results = input('Введите результаты игры в формате: '
                         'Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой: ').split(';')
    game_results[1] = int(game_results[1])
    game_results[3] = int(game_results[3])
    return game_results

def counting_results(game_results):
    list_team1 = [game_results[0], 0, 0, 0, 0, 0]
    list_team2 = [game_results[2], 0, 0, 0, 0, 0]
    if game_results[1] > game_results[3]:
        list_team1[1] += 1
        list_team1[2] += 1
        list_team1[5] += 3
        list_team2[1] += 1
        list_team2[4] += 1
    elif game_results[1] < game_results[3]:
        list_team1[1] += 1
        list_team1[4] += 1
        list_team2[1] += 1
        list_team2[2] += 1
        list_team2[5] += 3
    elif game_results[1] == game_results[3]:
        list_team1[1] += 1
        list_team1[3] += 1
        list_team1[5] += 1
        list_team2[1] += 1
        list_team2[3] += 1
        list_team2[5] += 1
    # print(list_team1)
    # print(list_team2)
    return list_team1, list_team2


def adding_results(dictionary_with_results):
    game_results = data_input()
    list_team1, list_team2 = counting_results(game_results)
    if list_team1[0] in dictionary_with_results.keys():
        previous_result = dictionary_with_results[list_team1[0]]
        for i in range(len(previous_result)):
            list_team1[i+1] += previous_result[i]
        dictionary_with_results[list_team1[0]] = list_team1[1:]
    else:
        dictionary_with_results[list_team1[0]] = list_team1[1:]
    if list_team2[0] in dictionary_with_results.keys():
        previous_result = dictionary_with_results[list_team2[0]]
        for i in range(len(previous_result)):
            list_team2[i+1] += previous_result[i]
        dictionary_with_results[list_team2[0]] = list_team2[1:]
    else:
        dictionary_with_results[list_team2[0]] = list_team2[1:]
    return dictionary_with_results


n = int(input('Введите количество завершенных игр: '))
dictionary_with_results = {}
for i in range(0, n):
    adding_results(dictionary_with_results)

for i in dictionary_with_results.items():
    team, result = i
    print(f'{team}: {result}')


