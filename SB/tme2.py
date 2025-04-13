from sympy import isprime, nextprime, randprime
from random import randint

def generate_q_prime(a, b):
    Q_prime = (b - a) // (b.bit_length() ** 2)
    Q_bit = Q_prime.bit_length()
    q_prime = 1
    p_k = 2
    list_pk = []
    while q_prime.bit_length() < Q_bit:
        q_prime *= p_k
        list_pk.append(p_k)
        p_k = nextprime(p_k)
    return list_pk, q_prime

def generate_p(a, b, q_prime, list_pk):
    while True:
        K = randint((a - 1) // q_prime, (b - 1) // q_prime)
        if isprime(K):
            p = 1 + q_prime * K
            if isprime(p) and a <= p < b:
                list_pk.append(K)
                return p

def generate_generator(p, q):
    while True:
        x = randint(2, p - 2)
        g = pow(x, (p - 1) // q, p)
        if g != 1:
            return g

a = int("eef9467ad3c124bb08b5fdf2e45cf800f3388a4d52909e8245190e8ff22c92fcca9f29ce4edafc06eff4bddb0640c22c8389ea0b9d207ee149ef194d36a5f9859492fabceeb9704fe7c51e7685dab42156c564a1cfa361ec7122eeb57ceab6583ea038096b6106bff82ea8ade9fb2a25bb9d781d40271869a19531556d056f08d8372fa50017e97a70d4daa37ea692f3430c421092a43364dbebaecd4540dc8324d6a38b0be6909f165f20486acb4555c6bf0f3472e737e751663f68d086372b66f21c5f5d16d7d78af0f51610d504913580d3c75691adf11fb3ab5b12e025e735109fb45c79458ae8bc2d06ccf88d7bff9b4d986f3174b380c6cc1e717538e7", 16)
b = a + 2**1950
q = int("eddc10b935806e01172f751701271362a37715291e477af9521c1ba736f58b7f05181653344dffe2f933b30b01a0cef", 16)

list_pk, q_prime = generate_q_prime(a, b)
p = generate_p(a, b, q_prime, list_pk)

g = generate_generator(p, q)

print(f"g = {g}")
print(f"(p-1) // q = {list_pk}")
