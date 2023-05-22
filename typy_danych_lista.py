lista = []  # tworzenie pustej listy

print(lista)  # []

lista.append("Radek")

print(lista)  # ['Radek']

lista.append("Tomek")
lista.append("Asia")
lista.append("Renata")
lista.append("Darek")
lista.append("Paweł")

print(lista)
# ['Radek', 'Tomek', 'Asia', 'Renata', 'Darek', 'Paweł']
print(lista[1])

# nadpisanie elementu o indeksie 1
lista[1] = "Magda"
print(lista)

# dopisanie elementu na indeksie 1, pozotałe o jeden w prawo
lista.insert(1, "Łukasz")
print(lista)
# ['Radek', 'Łukasz', 'Magda', 'Asia', 'Renata', 'Darek', 'Paweł']
lista.append("Asia")
lista.remove("Asia")
print(lista.remove("Asia"))
print(lista)

# pop - usuniecie po indeksie, zwraca element, który usunął
print(lista.pop(2))
print(lista)

# kopia listy
lista_copy = lista.copy()
print(lista.copy().__doc__)
lista_copy2 = lista  # kopia referencji !!! odwołanie do tego samego miejsca w pamieci
# usunie wszystko z listy
print(lista_copy2)
lista.clear()
print(lista)
print(lista_copy)
print(lista_copy2)
print(id(lista))  # przyblizone miejsce w pamieci
print(id(lista_copy2))
print(id(lista_copy))

liczby = [54, 999, 34, 22, 12.54, 876]
print(liczby)
liczby.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'
print(liczby)
liczby.reverse()
print(liczby)

liczby2 = liczby.copy()
print(liczby2)

liczby.clear()
print(liczby)

print(liczby2)

print(liczby2[:3])  # od indeksu 0 do 2
print(liczby2[2:])  # od 2 do konca
print(liczby2[:-1])  # 0d 0 do -1 czyli bez ostatniego
print(liczby2[:-2])  # od 0 do -2 (bez -2)

print(len(liczby2))  # zwraca długosc listy
liczby2.remove(54)
print(len(liczby2))

krotka = tuple(liczby2)
print(krotka)
print(type(krotka))  # <class 'tuple'>
