hex_p = "f1dbba1e9214829813aea078ad15c2465ae02ba3b2168500ecd900cd1bc87747d59d484f3c7d7d38530d7e7fe5d44b83254a29a685b2cff389aeca1a5e0a133b89427b4331b5899517ef32c85b807530920544dbb2764e594e33a50597878c0243a2a657966bfe155ce07433a4b29b69c84d509a2b63dd47d24315235a2ed73d"
p = int(hex_p, 16)

if p <= 1:
    racine = "p trop petit"
elif p % 4 != 1:
    racine = "p non congru à 1 mod 4"
else:
    expo = p // 4
    tentative = 2
    while True:
        base = tentative
        exposant = expo
        resultat = 1
        while exposant:
            if exposant % 2 == 1:
                resultat = resultat * base % p
                if resultat > p // 2:
                    resultat -= p
            base = base * base % p
            if base > p // 2:
                base -= p
            exposant //= 2

        val = resultat
        carre = val * val % p
        if carre > p // 2:
            carre -= p
        if carre == -1:
            racine = val
            break
        if carre != 1:
            racine = "probablement non premier"
            break
        tentative += 1

a = (p, 0)
b = (racine, 1)

while b != (0, 0):
    (a_re, a_im), (b_re, b_im) = a, b
    norme = b_re**2 + b_im**2
    produit_re = a_re * b_re + a_im * b_im
    produit_im = a_im * b_re - a_re * b_im

    produit_re_mod = produit_re % norme
    if produit_re_mod > norme // 2:
        produit_re_mod -= norme
    q_re = (produit_re - produit_re_mod) // norme

    produit_im_mod = produit_im % norme
    if produit_im_mod > norme // 2:
        produit_im_mod -= norme
    q_im = (produit_im - produit_im_mod) // norme

    r_re = a_re - b_re * q_re + b_im * q_im
    r_im = a_im - b_re * q_im - b_im * q_re

    a = b
    b = (r_re, r_im)

x, y = a
print(f"x = \n{x} \ny = \n{y}\n")
