import json
import binascii
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, ec
from cryptography.x509 import load_pem_x509_certificate
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend

def extraire_transactions(chemin_fichier):
    with open(chemin_fichier, 'r') as fichier:
        contenu = json.load(fichier)
    return contenu['batch']['transactions']

def verifier_authenticite(transaction):
    try:
        certificat_carte = load_pem_x509_certificate(transaction['card']['certificate'].encode(), default_backend())
        certificat_banque = load_pem_x509_certificate(transaction['card']['bank']['certificate'].encode(), default_backend())

        signature = binascii.unhexlify(transaction['signature'])
        contenu = transaction['data'].encode('utf-8')
        cle_publique_carte = certificat_carte.public_key()
        cle_publique_carte.verify(signature, contenu, ec.ECDSA(hashes.SHA256()))

        with open("cabank.pem", "rb") as fichier_ca:
            certificat_ca = load_pem_x509_certificate(fichier_ca.read(), default_backend())

        cle_pub_ca = certificat_ca.public_key()
        cle_pub_ca.verify(
            certificat_banque.signature,
            certificat_banque.tbs_certificate_bytes,
            padding.PKCS1v15(),
            certificat_banque.signature_hash_algorithm
        )

        certificat_banque.public_key().verify(
            certificat_carte.signature,
            certificat_carte.tbs_certificate_bytes
        )
        numero_attendu = transaction['card']['number']
        banque_attendue = transaction['card']['bank']['name']
        if numero_attendu not in transaction['data'] or banque_attendue not in transaction['data']:
            return 0

        return 1

    except Exception as erreur:
        print("Échec de vérification :", erreur)
        return 0

def lancement():
    transactions = extraire_transactions('transaction.json')
    verdicts = [verifier_authenticite(t) for t in transactions]
    print("Résultats des vérifications :\n", verdicts)

if __name__ == "__main__":
    lancement()
