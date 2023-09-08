# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [1, 2, 3, 4, 2, 3]
duplicates = []
unique_elements = set()

for item in my_list:
    if item not in unique_elements:
        unique_elements.add(item)
    else:
        duplicates.append(item)
print(unique_elements)
print(duplicates)