# klasa
import math


class MyFirstClass:
    """
    Reprezentuje punkty x i y
    """

    def __init__(self, x=0, y=0):
        """
        metoda inicjalizująca
        :param x:
        :param y:
        """

        self.move(x, y)

    def reset(self):
        self.move(0, 0)

    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def calculate(self, other: "MyFirstClass") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"x = {self.x}, y = {self.y}"


print(MyFirstClass.__doc__)

ob = MyFirstClass()
print(ob.x)
print(ob)
ob.move(45, 67)
print(ob)
print(ob.y)
# ob.move(0, 0)
ob.reset()
print(ob)
a = MyFirstClass(3, 5)
b = MyFirstClass(0, 5)

print(a)
print(b.calculate(a))
print(a.calculate(b))
assert b.calculate(a) == a.calculate(b)
a.move(3, 4)
print(a.calculate(b))
