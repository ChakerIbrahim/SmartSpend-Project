from Animal import Animal

class Lion(Animal):
    def __init__(self, name, age, size):
        super().__init__(name, age)
        self.size = size

    def feed(self):
        self.Happiness_level += 20
        self.Health_level += 5

    def display_info(self):
        super().display_info()
        print(f"size:{self.size}")
        print("-" * 30)

        return self
