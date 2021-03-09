from math import comb

k, n = map(int, input("k, n? ").split(" "))

def prob(k, n):
    def p(n):
        return comb(2**k, n) * 0.25**n * 0.75**(2**k - n)
    return 1 - sum(p(i) for i in range(n))

print(round(prob(k, n), 3))