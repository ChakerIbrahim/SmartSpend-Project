class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num

        for n in nums:
            self.result += n

        return self

    def subtract(self, num, *nums):
        self.result -= num

        for n in nums:
            self.result -= n

        return self


# create instance
md = MathDojo()

# test 1
x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)   # 5


# more tests
md2 = MathDojo()
print(md2.add(10).add(5, 5).subtract(3).result)

md3 = MathDojo()
print(md3.add(1, 2, 3, 4).subtract(2, 1).result)

md4 = MathDojo()
print(md4.subtract(10).add(20, 5).subtract(3, 2, 1).result)