import time
import functools  # Good practice to include this


def measure_time(func):
    @functools.wraps(func)  # Preserves the name and docstring of the original function
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time:.5f} seconds")
        return result  # Return the original function's result (if any)

    return wrapper  # Return the wrapper function, don't call it yet!


@measure_time
def do_something():
    count = 0
    # Increased range so the time is actually measurable
    for _ in range(1_000_000):
        count += 1
    print(f"Count: {count}")



def main():
    print("Measure time...")
    do_something()  # This now calls 'wrapper'



if __name__ == '__main__':
    main()