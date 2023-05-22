# for - pettla iteracyjna

lista = []
for i in range(6):  # 0..5
    print(i)
    if i % 2 == 0:  # reszta z dzielenia
        print("Jest parzysta", end='')
        lista.append(i)

print(lista)

lista2 = [j for j in range(6) if j % 2 == 0]
print(lista2)

for c in lista2:
    if c == 2:
        c += 1  # c = c + 1
    print(c)

# 15:00

imiona = ["Radek", "Zenek", "Monika"]

print(imiona)

for p in imiona:
    print(p)

# enumerate - zwraca element i indeks
for pozycja, osoba in enumerate(imiona):
    print(pozycja, osoba)

ludzie = ['Radek', 'Janek', 'Asia', 'Michał', 'Test']
wiek = [47, 67, 32, 34]

# łaczy w pary
for l, w in zip(ludzie, wiek):
    print(l, w)

for i, (o, w) in enumerate(zip(ludzie, wiek)):
    print(i, o, w)

for i in range(0, 10, 2):  # start, stop, krok 0..9
    print(i)

c = {'name': 'Radek', 'age': 5}
print({v: k for k, v in c.items()})

word = "Python"
letters = [letter for letter in word]
print(letters)

names = ['John', 'Alce', 'Bob']
ages = [25, 30, 35]
people = [(name, age) for name, age in zip(names, ages)]
print(people)
