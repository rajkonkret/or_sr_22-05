# dekorator
import time


def dekor(funk):
    def wew():
        print("Dekorujemy")
        return funk()

    return wew


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time} sec")
        return result

    return wrapper


@dekor
@measure_time
def hej():
    print("Hej")


@measure_time
def my_function():
    pass


hej()

dekor(hej())
my_function()
