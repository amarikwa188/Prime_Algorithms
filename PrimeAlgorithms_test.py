import unittest
from PrimeAlgorithms import trial_division, sieve_of_eratosthenes, dijkstra


class TestPrimeAlgorithms(unittest.TestCase):
    def test_trial_division(self):
        primes: list[int] = trial_division(30)[0]
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], primes)

    def test_sieve_of_eratosthenes(self):
        primes: list[int] = sieve_of_eratosthenes(30)[0]
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], primes)

    def test_dijkstra(self):
        primes: list[int] = dijkstra(30)[0]
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], primes)


if __name__ == "__main__":
    unittest.main()