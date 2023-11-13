# TODO Напишите функцию find_common_participants

def find_common_participants(first_group, second_group, delimiter=','):
    participants_from_first_group = set(first_group.split(delimiter))
    participants_from_second_group = set(second_group.split(delimiter))

    common_participants = list(participants_from_first_group.intersection(participants_from_second_group))
    common_participants.sort()

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

total = find_common_participants(participants_first_group, participants_second_group)
print(total)
# TODO Провеьте работу функции с разделителем отличным от запятой
