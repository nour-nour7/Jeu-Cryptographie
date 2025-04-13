from sympy import isprime, nextprime, mod_inverse
from sympy.ntheory.residue_ntheory import primitive_root
import random

a = int("ef913c51b9c950ebe2026b9840b819d08a7097b865eafd462023d898bd2126436c3c820d9c4653d673f8db5e04e030b41080cf986c1e2db1585e43cf6e9315b360d4a5b7f7b04ccc9b1cf3fc98a4d79de6537906fd8f7926fa686663fe5fe3759d089a72a7c174b2116e802898e5eddc3d7f8cf288fd8e2f6fa2476df20f2e3bd67ef3d1d54c3377f07b8984d611b4f147c4393a8088d4b7c24e858f239cac1242c41184d6d28082a2ec8e1c528f149c1d12c30d2e4605ec3d34f42d8ef4ce476f4d0e43ed1fd6c9902da6cd6217310bb74b0ae157382ebd8522feaebf9d8eb8c39e3eaab4f20e8e5051e0e20bfd20a11f75c4b60458b1546a9454192d0c0aa1", 16)
b = a + 2**1950
q = int("a9d28d99b19cd67095f64ce1b317157c896e8096fbc965c0a1304207ba97109f", 16)

def genere_p(a, b, q):
    while True:
        K = random.randint((a-1)//q, (b-1)//q)
        p = 1 + q * K
        if isprime(p):
            return p

def genere_g(p, q):
    while True:
        x = random.randint(2, p-2)
        g = pow(x, (p-1)//q, p)
        if g != 1:
            return g

p = genere_p(a, b, q)
print(f"p = {p}\n")

g = genere_g(p, q)
print(f"g = {g}\n")