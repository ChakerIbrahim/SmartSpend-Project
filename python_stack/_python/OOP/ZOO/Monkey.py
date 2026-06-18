from Animal import Animal

class Monkey(Animal):
    def __init__(self, name, age, favorite_food):
        super().__init__(name, age)
        self.favorite_food = favorite_food

    def feed(self):
        self.Happiness_level += 15
        self.Health_level += 20

    def display_info(self):
        super().display_info()
        print(f"favorite food:{self.favorite_food}")
        print("-" * 30)

        return self
