from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
import base64

public_key_pem = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1Jd+IDwsWU5wI/c8HYVn
Bfss82QGCv2AxjGMaK2pN5nMRMs8meyCrX55iFpRnK8jJO+iZglTDHGJV0T2T6Zq
IYl4Ia+9s7XI8H1afOLJ8VysZi2DZueqKo9jFVjTuMFWfNFgev/+xJo3rX2TY5Xl
LP1vEYMieny8pimgxY8reit4Ncdf/BFq7JqjR3TtzKa2LUp4HqTkwt1qGSW1U+Bu
1kCfM4dNMACCFVBwR3YKTRm5Oj2UHHan+3jhkoYWbAOTeCssTypjW2e8C7lQf1jI
fZlYmxCTfv3BHl8mHu06vXh3oK9x1UORUmE25wzhae5qazhOnLeWBOi8pzoIurrY
xwIDAQAB
-----END PUBLIC KEY-----
"""

public_key = RSA.import_key(public_key_pem)
cipher_rsa = PKCS1_OAEP.new(public_key)

session_key = get_random_bytes(16)

message = b"message"
cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(message)

enc_session_key = cipher_rsa.encrypt(session_key)

enc_session_key_b64 = base64.b64encode(enc_session_key).decode('utf-8')
ciphertext_b64 = base64.b64encode(ciphertext).decode('utf-8')
tag_b64 = base64.b64encode(tag).decode('utf-8')

print(f"Clé de session chiffrée (base64): {enc_session_key_b64}")
print(f"Message chiffré (base64): {ciphertext_b64}")
print(f"Tag (base64): {tag_b64}")