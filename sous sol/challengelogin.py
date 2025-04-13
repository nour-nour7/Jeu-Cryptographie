import subprocess


print("Déchiffrement du challenge...")
commande = "openssl enc -d -base64 -aes-128-cbc -pbkdf2 -pass pass:""134340Pluto"" -in CHAP_challenge.txt"

#commande = "ls"
res = subprocess.run(commande,capture_output=True,shell=True)

print("Les résultats :")
print(res.stdout)
print("Les erreurs :")
print(res.stderr)