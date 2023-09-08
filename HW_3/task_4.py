# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

items = {
    'Термос': 1,
    'Каремат': 2,
    'Кружка': 0.5,
    'Палатка': 3,
    'Ядовитый меч Уроборуса': 12,
    'Спальник': 2.5
}

max_weight = 2
backpack = []
current_weight = 0

for item, weight in items.items():
    if current_weight + weight <= max_weight:
        backpack.append(item)
        current_weight += weight


print("Вещи, которые влезут в рюкзак:")
for item in backpack:
    print(item)