import subprocess

# public key pour local electrique

print("Création de la clé publique et de la clé privé...")

creation = "openssl genpkey -algorithm RSA -out privkey.pem -pkeyopt rsa_keygen_bits:2048"

res_crea = subprocess.run(creation,shell=True,capture_output=True)

print(res_crea.stdout)
print(res_crea.stderr)

print("Extraction de la clé publique depuis le fichier...")

extraction = "openssl pkey -in privkey.pem -pubout -out pubkey_upload.pem "

res_extra = subprocess.run(extraction,shell=True,capture_output=True)

print(res_extra.stdout)
print(res_extra.stderr)

print("Terminé !")