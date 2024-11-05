def find_common_participants(group1, group2, delimiter=","):
    # Разбиваем строки участников на списки с использованием указанного разделителя
    participants1 = set(group1.split(delimiter))
    participants2 = set(group2.split(delimiter))

    # Находим пересечение участников и сортируем их
    common_participants = list(participants1.intersection(participants2))
    common_participants.sort()

    return common_participants


# Проверка работы функции
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверяем функцию с разделителем "|"
common = find_common_participants(participants_first_group, participants_second_group, delimiter="|")
print(common)
