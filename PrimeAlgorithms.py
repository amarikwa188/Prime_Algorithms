from math import sqrt
from time import perf_counter
import sys


def trial_division(num: int)-> list[int]:
    primes: list[int] = [2]
    for val in range(3, num+1):
        if val % 2 == 0: continue

        check, comp = 2, sqrt(val) 
        is_prime: bool = True
        while check <= comp:
            if val % check == 0:
                is_prime = False
            check += 1

        if is_prime: primes.append(val)
    
    space: int = sys.getsizeof(primes)
    
    return primes, space


def sieve_of_eratosthenes(num: int) -> list[int]:
    bool_array: list[bool] = [False] + [ True for _ in range(num-1)]
    primes: list[int] = []
    for number, val in enumerate(bool_array, 1):
        if not val:
            continue

        primes.append(number)

        if number > sqrt(num):
            continue

        for mul in range(2, (num // number)+1):
            index: int = mul*number - 1
            bool_array[index] = False

    space: int = sys.getsizeof(bool_array) + sys.getsizeof(primes)

    return primes, space 


def dijkstra(num: int) -> list[int]:
    pool: list[tuple[int]] = [[2,4]]
    primes: list[int] = [2]

    for val in range(3, num+1):
        if val < pool[0][1]:
            primes.append(val)
            if val**2 <= num:
                pool.append([val, val**2])
        else:
            for idx in range(len(pool)):
                n, factor = pool[idx]
                if factor > val: break
                pool[idx][1] = factor + n
        pool.sort(key=lambda tup: tup[1])

    space: int = sys.getsizeof(pool) + sys.getsizeof(primes)

    return primes, space


if __name__ == "__main__":
    print("Prime Findng Algorithms")
    print("-----------------------")
    print("This is a program to find all the primes up to a certain number. "
          "It showcases the Trial Division, Sieve of Erastothenes and "
          "Dijkstra's prime finding algorithms.\n")

    limit_string: str = input("Enter a number:\n>").strip()
    while True:
        try:
            limit: int = int(limit_string)
            break
        except:
            print("Invalid input: please enter a number.")
            limit_string: str = input("Enter a number:\n>").strip()
    
    print("\n---Trial Division---")
    t1 = perf_counter()
    print("Primes: ", end="")
    primes, space = trial_division(limit)
    print(*primes, sep=", ")
    print(f"Space: {space} bytes")
    print(f"Time: {perf_counter() - t1} seconds\n")

    print("\n---Sieve of Erastothenes---")
    t1 = perf_counter()
    print("Primes: ", end="")
    primes, space = sieve_of_eratosthenes(limit)
    print(*primes, sep=", ")
    print(f"Space: {space} bytes")
    print(f"Time: {perf_counter() - t1} seconds\n")

    print("\n---Dijkstra's Algorithm---")
    t1 = perf_counter()
    print("Primes: ", end="")
    primes, space = dijkstra(limit)
    print(*primes, sep=", ")
    print(f"Space: {space} bytes")
    print(f"Time: {perf_counter() - t1} seconds\n")