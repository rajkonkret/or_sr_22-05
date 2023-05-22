# set - przechowuje niepowtarzające sie elementy

lista = [44, 55, 66, 77, 33, 22, 11, 55, 33, 11]
print(lista)

zbior = set(lista)
print(zbior)
print(type(zbior))  # <class 'set'>

zbior1 = set()  # pusty set
print(zbior1)
print(type(zbior1))

zbior1.add("1")
print(zbior1)

zbior.add(18)
zbior.add(18)
zbior.add(62)
print(zbior)
print(zbior.pop())
print(zbior.pop())
print(zbior.pop())
print(zbior)

zbior_liczb = {66, 11, 44, 18, 55, 62, 999}
print(zbior_liczb)
print(type(zbior_liczb))  # <class 'set'>

lista2 = list(zbior_liczb)
print(lista2)
zbior_test = set(lista2)
print(zbior_test)

print(zbior | zbior_test)  # suma zbiorów
print(zbior & zbior_test)  # cześć wspolna
print(zbior - zbior_test)  # różnica

print(zbior.difference(zbior_test))
print(zbior)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
new_set = set1 | set2  # nowy set z zawartoscią obu zbiorów
print(new_set)
print(set1, set2)

# update - dodanie z set2 do set1(set1 ma nowa zawartosc)
set1.update(set2)
print(set1)

# nowy set z zawartoscia set1 i set2 - suma zbiorów
set1 = {1, 2, 3}
new_set2 = set(set1).union(set2)
print(new_set2)
print(set1)
