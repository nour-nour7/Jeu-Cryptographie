import subprocess

print("============Tutoriel============")

print("Chiffré le message...")

print("Chiffrage terminé")

# Commande pour chiffré un message à partir d'une clé publique
chiffre = f"openssl pkeyutl -encrypt -in pki_tutorial_a_chiffrer.txt -pubin -inkey pki_tutorial_public_key.pem"
        # On utilise xxd -r pour revert

res = subprocess.run(chiffre,shell = True, capture_output=True)
chiffre_txt = res.stdout.hex()

print(chiffre_txt)
print(res.stderr)

# On enregistre le résultat dans un fichier
with open("pki_tutorial_chiffre.txt",'w') as f:
    f.write(chiffre_txt)

