from concurrent.futures import ProcessPoolExecutor

def is_odd_number(number):
    return number % 2

executor = ProcessPoolExecutor()
it = executor.map(is_odd_number, [1, 2], timeout=1)
print(next(it))
print(next(it))