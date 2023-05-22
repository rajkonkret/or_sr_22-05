print("Radek")  # str
# pep8
# ctrl alt l - wyrównanie

# zmienna - pudełko na dane
imie = "Radek"
print(imie)
print(type(imie))  # <class 'str'>
imie = 39
print(imie)
print(type(imie))  # <class 'int'>
a = 6  # int
b = "7"  # str
print(a * b)

wiek = 47  # int
rok = 2023  # int
temp = 36.6  # float - zmiennoprzecinkowy
print(0.1 + 0.7)  # 0.7999999999999999, oczekiwany 0.8
print(wiek * rok)
print(wiek - rok)
print(wiek + rok)
print(wiek / rok)  # 0.023232822540781017 - w wyniku float
print(wiek // rok)  # częśc całkowita z dzielenia
print(wiek % rok)  # modulo, czyli reszta
print(wiek ** rok)  # potęgowanie
print(54 - 5 * 43 + 4 / 2 * 4 / 2)  # ctrl d - powielenie lini
print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # ctrl d - powielenie lini
print(54 - (5 * 43) + (4 / 2 * 4) / 2)
print(54 - (5 * 43) + (4 / 2 + 4) / 2)

print("\tSprawdzam zmienną temp: {} {}\n".format(wiek, temp))
print(f"\tSprawdzam zmienną temp {wiek} {temp}")
print(f"""
    zmienna {temp}
    zmienna {wiek}
""")
imie = "Radek Radek"
imie2 = imie.lower()
print(imie)
print(imie2)
print(imie.upper())
print(imie)

print(imie.capitalize())
print(imie.count("Radek"))

# boolean - zmienna logiczna
czy_znasz_Python = True  # prawda <class 'bool'>
czy_znasz_Python = False  # fałsz <class 'bool'>

print(type(czy_znasz_Python))
print(int(czy_znasz_Python))
# fałsz = 0 , prawda = wszytko różne od 0
false = -1
print(bool(false))  # True
"""
Komentarz wielolinijkowy
"""
# 11:25