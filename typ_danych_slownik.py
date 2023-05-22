# słownik (dict) - klucz - wartosć
# { "name" : "Radek"} przypomna json

slownik = {}  # pusty słownik
print(type(slownik))  # <class 'dict'>

slownik['imie'] = "Raddek"
slownik['wiek'] = 39

# {'imie': 'Raddek', 'wiek': 39}
print(slownik)

print(slownik['imie'])

slownik['imie'] = "Tomek"
print(slownik)
slownik['imie'] = ["Radek", "Tomek"]
print(slownik)
slownik.update({"imie": "Tomek"})
print(slownik)
slownik['imie'] = ["Radek", "Tomek"]

print(slownik['imie'][0])

slownik2 = {'imie': 'Radek', "kot": "cat"}
print(slownik2)

# stworzyc słownik polsko -angielski z uzyciem dict
slownik3 = {'name': 'imie', 'cat': 'kot'}
print(slownik3['cat'])

print(slownik.keys())
print(slownik.values())
print(slownik.items())

print("Umiem przetłumaczyć", slownik3.keys())
key = input("Podaj wyraz")
# pobranie ze słownika z wartością domyslną
value = slownik3.get(key.lower().replace(" ", ''), "Nie ma w słowniku")
print(value)
