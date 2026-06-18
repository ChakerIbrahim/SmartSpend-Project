class Animal:
    def __init__(self, name, Age, Health_level=100, Happiness_level=100):
        self.name = name
        self.Age = Age
        self.Health_level = Health_level
        self.Happiness_level = Happiness_level

    def display_info(self):
        print(
            f"Name:{self.name} - Health level: {self.Health_level} - Happiness level:{self.Happiness_level}"
        )
        return self

    def feed(self):
        self.Health_level += 10
        self.Happiness_level += 10
        return self
