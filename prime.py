import math


class Prime:
    def __init__(self):
        self._primes = self.get_primes()
        self._max = max(self._primes)

    @staticmethod
    def get_primes():
        with open('primes') as fd:
            return list(map(int, fd.read().split(',')))

    def set_primes(self):
        with open("primes", 'w') as fd:
            fd.write(",".join([str(i) for i in self._primes]))

    def is_prime(self, number):
        if number <= self._max:
            return number in self._primes

        for i in range(2, math.isqrt(number)):
            if number % i == 0:
                return False
        return True

    def sieve(self, number):
        if number <= self._max:
            return number in self._primes

        primes = [True] * (number + 1)
        primes[0], primes[1] = False, False

        for i in range(2, math.isqrt(number) + 1):
            for j in range(i * i, number + 1, i):
                primes[j] = False

        self.bool_to_primes(primes)
        return number in self._primes

    def bool_to_primes(self, bools):
        result = []
        for i in range(len(bools)):
            if bools[i]:
                result.append(i)
        self._primes = result
        self.set_primes()


if __name__ == "__main__":
    obj = Prime()
    print(obj.sieve(121))
