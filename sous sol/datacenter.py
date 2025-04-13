import subprocess

# en cas de problème, cette exception est déclenchée
class OpensslError(Exception):
        pass

    # Il vaut mieux être conscient de la différence entre str() et bytes()

# On décrypte la clé d'abord en utilisant le mot sur le post-it comme mot de passe
decrypt_pkey = "openssl enc -aes-128-cbc -d -base64 -pbkdf2 -pass pass:"'ISECR0XX'" -in encrypted.txt -out decrypted.txt"

res = subprocess.run(decrypt_pkey,shell=True,capture_output=True)
print(res,"\n\n")
