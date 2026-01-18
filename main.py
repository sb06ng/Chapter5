import functools
import time


def log_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        print(
            f"{func.__name__} was called with the following arguments: {args}, {kwargs}. And returned: {return_value}")
        return return_value

    return wrapper


def measure_time(func):
    @functools.wraps(func)  # Preserves the name and docstring of the original function
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time:.5f} seconds")
        return result

    return wrapper


@log_function
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


@log_function
@capitalize_strings
def greet_user(name, age, city):
    print(f"Hello {name}, I see you are from {city} and you are {age} years old.")


def main():
    print("Measure time...")
    do_something()  # This now calls 'wrapper'
    print("Capitalize arguments")
    greet_user("john", 23, city="new york")


if __name__ == '__main__':
    main()
