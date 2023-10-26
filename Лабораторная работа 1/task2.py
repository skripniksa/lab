list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

count = len(list_players)
half = count // 2

first_team = list_players[:half]
second_team = list_players[half:]

print(first_team)
print(second_team)