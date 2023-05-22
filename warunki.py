# warunki czyli instrukcje sterowania przepływem programu

czy_znasz_Python = False

# wcięcie obowiązkowe po :
if czy_znasz_Python:
    print("Super")
else:
    print("Idź się uczyć")

if czy_znasz_Python:
    pass

print("Dalsza częśc programu")

name = "Tomek"

if name == "Radek":
    print(f"Twoje imię {name}")

# := naipierw przypisuje do zmiennej, a potem przyrównuje
if name := "Radek":
    print(f"Twoje imię {name}")  # fstring

podatek = 0.0
zarobki = int(input("Podaj swoj dochód"))  # input zawsze zwraca str

if zarobki < 10000:
    podatek = 0.0
elif zarobki < 30000:
    podatek = 0.3
elif zarobki < 100000:
    podatek = 0.4
else:
    podatek = 0.7

print(f"Zapłacisz {zarobki * podatek} zł")
