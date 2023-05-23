from name_function import get_formatted_name

print("Wpisz q by zakończyc")

while True:
    first = input("Podaj imię")
    if first == 'q':
        break
    second = input("Podaj drugie imie")
    if second == 'q':
        break
    last = input("Podaj nawisko")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last, second)
    print(f"Sformatowane {formatted_name}")
