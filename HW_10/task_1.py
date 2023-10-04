# Доработаем задания 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.spec = None

    def get_spec(self):
        return self.spec


class Fish(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec


class Cat(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec


class Dog(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec


class AllAnimal(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec


class AnimalFactory(AllAnimal):
    def __init__(self, animal_type, name=None, age=None, spec=None):
        self.animal_type = animal_type
        AllAnimal.__init__(self, name, age, spec)

    def create_animal(self, *args, **kwargs):
        if self.animal_type == "Cat":
            return Cat(*args, **kwargs)
        elif self.animal_type == "Dog":
            return Dog(*args, **kwargs)
        elif self.animal_type == "Fish":
            return Fish(*args, **kwargs)
        else:
            raise ValueError("Некорректный тип животного")


# Пример использования
animal_cat_1 = AnimalFactory("Cat").create_animal("Murky", 2, "May!!")
animal_cat_2 = AnimalFactory("Cat").create_animal("Murza", 2, "May!!")
animal_cat_3 = AnimalFactory("Cat").create_animal("Mupo", 2, "May!!")
animal_cat_4 = AnimalFactory("Cat").create_animal("Lola", 2, "May!!")
print(animal_cat_1.name, animal_cat_1.age, animal_cat_1.get_spec())
print(animal_cat_2.name, animal_cat_2.age, animal_cat_2.get_spec())
print(animal_cat_3.name, animal_cat_3.age, animal_cat_3.get_spec())
print(animal_cat_4.name, animal_cat_4.age, animal_cat_4.get_spec())

animal_Fish_1 = AnimalFactory("Fish").create_animal("Stars", 1, "Swiming!!")
print(animal_Fish_1.name, animal_Fish_1.age, animal_Fish_1.get_spec())
