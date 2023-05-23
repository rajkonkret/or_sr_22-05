def multi(a, b):
    try:
        return int(a) * int(b)
    except ValueError:
        return "Zwracam bezpieczne 0"
    except TypeError:
        return "Błedne dane"


print(multi(5, 5))
print(multi("5", "3"))
print(multi(5, "A"))
print(multi((3,), 9))
print("Działam dalej")


# metoda zielenie i przetestowac dzielenie przez zero
def dzielenie(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return "Zwracam bezpieczne 0"
    except TypeError:
        return "Błedne dane"
    except ZeroDivisionError:
        return "Nie dzielimy przez zero"


print(dzielenie(2, 0))
print("Program nadal działa")


def multi2(a, b):
    try:
        return int(a) * int(b)
    except Exception as e:
        return f"błędne dane - błąd {e.args}"


print(multi2(3, "A"))
print("Program nadal działa")

valid_data = [{'name': 'Jan', "age": '10'}, {'name': 'DAwid', "age": '25'}, {'name': 'Marcin', "age": '23'}]
invalid_data = [{}, {'name': 'DAwid', "age": '25'}, {'name': 'Marcin', "age": '23'}]
invalid_data2 = [{'name': 'Jan', "age": 'age'}, {'name': 'DAwid', "age": '25'}, {'name': 'Marcin', "age": '23'}]


def check_age(users, age):
    count = 0
    for i, user in enumerate(users):
        try:
            user_age = int(user['age'])
        except Exception as e:
            print(f"Niepoprawne dane")
        else:  # gdy nie ma błedu
            count += 1 if user_age < age else 0
        finally:  # wykona sie zawsze
            print(f"{i}--{user}")
    return f"Ilośc osób spełniająca kryteria: {count}"


print(check_age(valid_data, 15))
print(check_age(invalid_data, 15))
print(check_age(invalid_data2, 15))
