import subprocess

print("Signature")

sign_chal = "openssl dgst -sha256 -hex -sign privkey.pem -out signature.txt challenge.txt"

res_sign = subprocess.run(sign_chal,shell=True,capture_output=True)

print(res_sign.stdout)
print(res_sign.stderr)