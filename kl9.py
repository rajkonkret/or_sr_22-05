# class MyException(Exception):
#     def __init__(self, message):
#         super().__init__(message)
#
#
# raise MyException("Wystąpił bład!")

class MyException(ValueError):
    pass


try:
    x = int(input("Podaj liczbę całkowitą"))
    if x < 0:
        raise MyException("Liczba dni musi być dodatnia")
except MyException as e:
    print("Wystąpił mój własny wyjątek", e)
except ValueError as e:
    print("Wystapił bład ValueError")
