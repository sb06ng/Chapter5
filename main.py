import functools
import time


def measure_time(func):
    @functools.wraps(func)  # Preserves the name and docstring of the original function
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time:.5f} seconds")
        return result

    return wrapper


@measure_time
def do_something():
    count = 0
    # Increased range so the time is actually measurable
    for _ in range(1_000_000):
        count += 1
    print(f"Count: {count}")


def capitalize_strings(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        new_args = []
        for arg in args:
            try:
                new_args.append(arg.capitalize())
            except AttributeError:
                new_args.append(arg)
        new_kwargs = {}
        for key, value in kwargs.items():
            try:
                new_kwargs[key] = value.capitalize()
            except AttributeError:
                new_kwargs[key] = value
        return func(*tuple(new_args), **new_kwargs)

    return wrapper


@capitalize_strings
def greet_user(name, age, city):
    print(f"Hello {name}, I see you are from {city} and you are {age} years old.")


def main():
    print("Measure time...")
    do_something()  # This now calls 'wrapper'
    print("Capitalize arguments")
    greet_user("john", 23, "new york")


if __name__ == '__main__':
    main()
