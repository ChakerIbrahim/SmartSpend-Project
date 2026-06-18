from Animal import Animal
from Lion import Lion
from Monkey import Monkey
from Bear import Bear


class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        return self

    def feed_all_animals(self):
        for animal in self.animals:
            animal.feed()
        return self

    def print_all_info(self):
        print("-" * 30, self.name, "-" * 30)
        for animal in self.animals:
            animal.display_info()
        return self


zoo1 = Zoo("Jalil's & Murad Zoo")

lion = Lion("Simba", 5, "Large")
monkey = Monkey("Momo", 3, "Banana")
bear = Bear("Willy", 7, "Brown")

zoo1.add_animal(lion)
zoo1.add_animal(monkey)
zoo1.add_animal(bear)

zoo1.feed_all_animals()
zoo1.print_all_info()
