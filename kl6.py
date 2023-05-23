import pickle
from dataclasses import dataclass


# pomaga przy pracy z obiektami

@dataclass
class Person:
    first_name: str
    last_name: str
    id: int

    def greet(self):
        print(f"Witam, jestem {self.first_name} {self.last_name}, Id to {self.id}")


people = [
    Person("JAcek", "Kowalski", 1),
    Person("Mateusz", "Zegar", 2)
]
# [Person(first_name='JAcek', last_name='Kowalski', id=1), Person(first_name='Mateusz', last_name='Zegar', id=2)]
print(people)

with open('data.pickle', 'wb') as stream:
    pickle.dump(people, stream)

with open('dane.txt', 'w') as stream:
    stream.write(str(people))
