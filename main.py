import timeit
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Генерація тестових масивів
random_arr = [random.randint(0, 1000) for _ in range(10000)]

# Функція для заміру часу
def measure_time(func, arr, is_builtin=False):
    if is_builtin:
        setup_code = f"""
import random
arr = random.sample(range(10000), 10000)  # Генерація нового масиву для кожного виклику
        """
        test_code = f"{func.__name__}(arr)"
    else:
        setup_code = f"""
from __main__ import {func.__name__}
import random
arr = random.sample(range(10000), 10000)  # Генерація нового масиву для кожного виклику
        """
        test_code = f"{func.__name__}(arr)"

    times = timeit.repeat(stmt=test_code, setup=setup_code, number=1, repeat=5)
    return sum(times) / len(times)

# Замір часу для функцій
print("Insertion Sort:", measure_time(insertion_sort, random_arr), "seconds")
print("Merge Sort:", measure_time(merge_sort, random_arr), "seconds")
print("Timsort (sorted):", measure_time(sorted, random_arr, is_builtin=True), "seconds")
