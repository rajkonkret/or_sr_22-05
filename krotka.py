# krotka - tuple -
# krotka kolekcja, niezmienna
# zmienna, niezmienna - jednoelementowa krotka
# indexy liczone od 0, 0, 1, 2, 3
tupla = ("Tomek", "Michał", "Asia", "Daniel")
tupla2 = ("Radek",)
tupla3 = 44, 34, 22.43, 11, 200

print(tupla)
print(type(tupla))  # <class 'tuple'>
print(tupla2)
print(type(tupla2))  # <class 'tuple'>

print(tupla3)
print(type(tupla3))

print(tupla.count("Tomek"))
print(tupla.index("Asia"))  # index = 2
asia = tupla[2]
print(asia)

a, b = 1, 2  # a =1, b = 2
print(a)
a, b = b, a  # a = b , b = a
print(a, b)
x = 1, 2, 3  # <class 'tuple'>
print(type(x))
a, *b = 1, 2, 3
print(a)
print(b)

# rozpakowanie tupli
# * wskazuje na worek inne
imie, *imie2, imie3 = tupla
print(imie)
print(imie2)
print(imie3)
print(type(imie2))  # <class 'list'>

lista = list(tupla)  # rzutowanie na liste
print(lista)
