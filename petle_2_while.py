# while - petla sterowana warunkiem

licznik = 0
while True:
    licznik += 1
    print("Komunikat!!!")
    if licznik > 10:
        break  # przrwanie działania pętli

print(licznik)
licznik = 0
while licznik < 10:
    print("komunikat2")
    licznik += 1

lista = []
while True:
    wej = input("podaj liczbe")
    if not wej.isnumeric():
        break
    lista.append(int(wej))

print(lista)