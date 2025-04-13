#!/usr/bin/env python3
import subprocess
import sys
import binascii

def sign_challenge(challenge_text, private_key_file="privkey.pem"):
    """
    Signs a challenge text with a private key and returns a hex-encoded signature.
    
    Args:
        challenge_text (str): The challenge text to sign
        private_key_file (str): Path to the private key file
        
    Returns:
        str: Hex-encoded signature
    """
    # Write challenge to a temporary file
    with open("temp_challenge.txt", "w") as f:
        f.write(challenge_text)
    
    # Sign the challenge using OpenSSL
    command = ["openssl", "dgst", "-sha256", "-sign", private_key_file, "temp_challenge.txt"]
    result = subprocess.run(command, capture_output=True)
    
    if result.returncode != 0:
        print("Error signing challenge:")
        print(result.stderr.decode())
        return None
    
    # Convert binary signature to hex
    hex_signature = binascii.hexlify(result.stdout).decode('ascii')
    return hex_signature

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python sign_challenge.py 'challenge text'")
        sys.exit(1)
    
    challenge = sys.argv[1]
    print(f"Challenge: {challenge}")
    
    signature = sign_challenge(challenge)
    if signature:
        print("\nHex-encoded signature:")
        print(signature)
        print("\nCopy the above signature to use with the armoire system.")