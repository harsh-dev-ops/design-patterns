import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(
            f'Function {func.__name__} took {round((end - start)*1000, 2)} ms to run.')

        return result

    return wrapper


@time_it
def add(a, b):
    return a + b


if __name__ == '__main__':
    add(1, 2)
