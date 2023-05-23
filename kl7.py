import pickle
from kl6 import Person

with open('data.pickle', 'rb') as stream:
    p = pickle.load(stream)

print(p)
print(type(p))  # <class 'list'>

for person in p:
    person.greet()

with open('dane.txt', 'r') as stream:
    p2 = stream.read()

print(p2)
print(type(p2))  # <class 'str'>
print(p2.replace("[", ""))
print(p2.replace("]", ""))
