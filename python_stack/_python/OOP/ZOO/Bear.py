from Animal import Animal

class Bear(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def feed(self):
        self.Happiness_level += 8
        self.Health_level += 12
        return self

    def display_info(self):
        super().display_info()
        print(f"Bear Color:{self.color}")
        print("-" * 30)

        return self
