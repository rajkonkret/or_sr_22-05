lang = input("Wpisz znany Ci język programowania")
lista = []

match lang:
    case "python":
        lista.append(lang)
    case "java":
        lista.append(lang)
    case _:  # wartość domyślna
        print("Nie znam takiego języka")

print(lista)