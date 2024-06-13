import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"\nFunction {func.__name__} took {(end_time - start_time):.6f} seconds to run.")
        return result
    return wrapper