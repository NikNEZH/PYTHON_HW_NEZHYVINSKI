# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

friends_items = {
    "Никита": ("аптечка", "меч", "спальник"),
    "Пабло": ("спички", "аптечка", "спальник"),
    "Александр": ("спички", "аптечка", "спальник")
}

# Какие вещи взяли все три друга
common_items = set.intersection(*map(set, friends_items.values()))
print("Вещи, которые взяли все три друга:", common_items)

# Какие вещи уникальны, есть только у одного друга
unique_items = set.difference(*map(set, friends_items.values()))
print("Уникальные вещи, есть только у одного друга:", unique_items)

# Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
missing_items = []
missing_name = []
for item in friends_items.values():
    i = 0
    count = 0
    friend_without_item = ''
    for friend, items in friends_items.items():
        print(items[i])
        print('')
        print(item[i])
        if item[0] not in items[i]:
            count += 1
            friend_without_item = friend
        if count == len(friends_items) - 1:
            if item not in missing_items:
                missing_items.append(item)
                missing_name = {friend_without_item}
        i += 1
print(i)
print(F'"Вещи, которые есть у всех друзей {missing_items} кроме одного и имя друга, у которого данная вещь отсутствует:{missing_name}"')

"""
Это очень плохой код я знаю у меня не очень хорошо получилось понять эту тему я буду очень рад за помощь чтобы 
разобраться спасибо и еще раз простите

"""