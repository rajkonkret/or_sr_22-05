import random

print(random.randint(1, 6))  # int 1..6
print(random.random())  # float 0 do 0.9999999999999
print(random.randrange(6))  # int 0..5
print(random.randrange(1, 6))  # int 1..5

lista = [5, 7, 6, 45, 34, 56]
print(random.choice(lista))

lista2 = list(range(1, 50))  # 1..49
print(lista2)

print(random.choice(lista2))
print(random.choice(lista2))
print(random.choice(lista2))
print(random.choice(lista2))
print(random.choice(lista2))
print(random.choice(lista2))

print(random.choices(lista2, k=6))
# wtym przypadku liczby sie nie powtórzą
print(random.sample(lista2, k=6))
