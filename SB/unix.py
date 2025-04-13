from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util import number
import binascii

def pkcs1v15_padding(message, key_size):
    message_int = int(binascii.hexlify(message.encode()), 16)
    block_size = key_size - 11
    padding = b'\x00\x02' + get_random_bytes(block_size - len(message)) + b'\x00'
    padded_message = padding + message.encode()
    return int(binascii.hexlify(padded_message), 16)

def sign_with_mask(public_key, message):
    key = RSA.import_key(public_key)
    n = key.n  
    e = key.e

    key_size = (n.bit_length() + 7) // 8

    padded_message = pkcs1v15_padding(message, key_size)
    
    x = number.getRandomRange(1, n - 1)
    
    masked_message = (padded_message * pow(x, e, n)) % n
    
    masked_message_hex = hex(masked_message)[2:].upper() 
    
    return masked_message_hex, x

message = "I, the lab director, hereby grant nour permission to take the BiblioDrone-NG."

public_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvtbNyPFC1hhUtr3cb56z
a7v05dq3cgckAHgpPDhOtT1OOgsvJQ1t0RkkSJc7JQ1WNRchjJChLARH9bMd83QQ
2KLiFXPA8FqKqZJBFHCAU7CIeNO1PM01ujUWwCw2ktBIrUbpi3++E6mbRnD8yW3V
HnoEo9qTSTq1tbD/eud3CNdPjJZBElI/7VnBvclJv+okj/CjkoUwKwKSprjeI/mK
kgE1zxtWYOFutP3bsktDEu9cWfSgKmff8rKKbRsMPjlCwXNvqkOpTwmV4EvabIc6
HLr2aFQkGWq8YYXT5A/BzCdvrnLeBGXZdI5ut+FltigApT8sZ+RpPMkrN6nuS8RJ
6QIDAQAB
-----END PUBLIC KEY-----"""

masked_message_hex, x = sign_with_mask(public_key, message)
print(f"Masquage du message (hex) : {masked_message_hex}")
print(f"Valeur x : {x}")
