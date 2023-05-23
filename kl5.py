from abc import ABC, abstractmethod


class Counter(ABC):
    def __init__(self, values=0):
        self.values = values

    @abstractmethod
    def drukuj(self):
        pass

    def increment(self, by=1):
        self.values += by  # values=values+by

    # metoda statyczna
    # nie potrzebuje obiektu. jest wywoływana z kalsy
    @staticmethod
    def format_string():
        return '%d'

    @classmethod
    def from_other(cls, counter):
        return cls(counter.values)


class BoundedCounter(Counter):
    MAX = 100

    def __init__(self, values=0):
        if values > self.MAX:
            # raise - rzucenie wyjątku
            raise ValueError("Wartość nie może przekroczyc MAX")
        super(BoundedCounter, self).__init__(values)

    def drukuj(self):
        print("Drukuje...", self.values)


# c = Counter()
# c.increment()
# print(c)
# c.drukuj() - klasa abstrakcyjna, nie można stworzyc obiektu klasy
b = BoundedCounter()
b.drukuj()
# b2 = BoundedCounter(102) - rzuci wyjątek
print(Counter.format_string())
b.increment()
b.drukuj()
c = BoundedCounter.from_other(b)  # <class '__main__.BoundedCounter'>

c.drukuj()
print(type(c))
