import random
from sympy import factorint
import json
a_hex = "458a1b615fe828c655ca102013c45bb263d602b74c059fd5e534bb5dbd3439994674b721e3c4be83ecce48aa805d4481b6508c45825689ed4edbaa6265041726d2f4448221e99b704a1c98e84b75eb434bf1c2b941278606b33e7f6ceeb9c321bd16b829896ec7fa02fd8886d37766cca217938a553574b449b732edf1558cc"
a = int(a_hex, 16)
b = a + 2**960

taille_octets = (b.bit_length() + 7) // 8

liste_pk = [2]
Q_prime = 2
c = 20000
max_Q_prim = (b - a) // (c * taille_octets**2)

while ((max_Q_prim.bit_length() + 7) // 8) != ((Q_prime.bit_length() + 7) // 8):
    borne_sup = min(pow(2, 160), pow(2, 8 * (((max_Q_prim.bit_length() + 7) // 8) - ((Q_prime.bit_length() + 7) // 8))))
    pi = random.randrange(2, borne_sup)
    
    if pi % 2 == 0 or pi in (0, 1):
        continue
    r, s = 0, pi - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    est_premier = True
    for _ in range(10):
        a_mr = random.randrange(2, pi - 1)
        x = pow(a_mr, s, pi)
        if x in (1, pi - 1):
            continue
        for _ in range(r - 1):
            x = pow(x, 2, pi)
            if x == pi - 1:
                break
        else:
            est_premier = False
            break
    if est_premier:
        Q_prime *= pi
        liste_pk.append(pi)

borne_inf = a // Q_prime
borne_sup = b // Q_prime
p_k = random.randrange(borne_inf, borne_sup)
while True:
    def est_probablement_premier(n):
        if n % 2 == 0 or n in (0, 1):
            return False
        r, s = 0, n - 1
        while s % 2 == 0:
            r += 1
            s //= 2
        for _ in range(1):
            a_mr = random.randrange(2, n - 1)
            x = pow(a_mr, s, n)
            if x in (1, n - 1):
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

    if est_probablement_premier(p_k) and est_probablement_premier(Q_prime * p_k + 1):
        break
    p_k = random.randrange(borne_inf, borne_sup)

liste_pk.append(p_k)
p = 1
for facteur in liste_pk:
    p *= facteur
p += 1

while True:
    g = random.randrange(2, p - 1)
    if all(pow(g, (p - 1) // q, p) != 1 for q in liste_pk):
        break

def certificat_pratt(liste_facteurs):
    certificat = []
    for facteur in liste_facteurs:
        entree = {'p': facteur}
        if facteur >= 1024:
            sous_facteurs = []
            facteurs_pm1 = factorint(facteur - 1)
            for base, exp in facteurs_pm1.items():
                sous_facteurs.extend([base] * exp)
            while True:
                g_sub = random.randrange(2, facteur - 1)
                if all(pow(g_sub, (facteur - 1) // d, facteur) != 1 for d in sous_facteurs):
                    break
            entree['g'] = g_sub
            entree['pm1'] = certificat_pratt(sous_facteurs)
        certificat.append(entree)
    return certificat

certificat_final = {
    'p': p,
    'g': g,
    'pm1': certificat_pratt(liste_pk)
}

with open('certificat_pratt.json', 'w') as fichier:
    json.dump(certificat_final, fichier)

print(json.dumps(certificat_final))
print("certificat généré et sauvegardé dans certificat_pratt.json")
