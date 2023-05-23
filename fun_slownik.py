slownik = {'name': 'Radek'}


def build_person(first, last, age=None):
    person = {'first': first, 'last': last}
    if age:
        person['age'] = age

    return person


while True:
    print("Podaj imię i nazwisko")
    print("Wpisz q by zakończyc")
    f_name = input("IMIĘ: ")
    if f_name == 'q':
        break
    l_name = input("NAZWISKO: ")
    if l_name == 'q':
        break
    age = input("WIEK: ")
    if age == 'age':
        break
    print(build_person(f_name, l_name, age))
