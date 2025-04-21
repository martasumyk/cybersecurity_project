import subprocess
import os

# Set the path to your OpenSSL executable
OPENSSL_PATH = r"C:\Program Files\OpenSSL-Win64\bin\openssl.exe"

# Check if OpenSSL exists at the given path
if not os.path.exists(OPENSSL_PATH):
    print(f"[!] OpenSSL not found at {OPENSSL_PATH}")
    print("[!] Please ensure OpenSSL is installed and the path is correct.")
    exit(1)

def generate_rsa_keys(private_key_path="private_key.pem", public_key_path="public_key.pem", key_size=4096):
    try:
        # Generate private key
        subprocess.run([
            OPENSSL_PATH, "genpkey",
            "-algorithm", "RSA",
            "-out", private_key_path,
            "-pkeyopt", f"rsa_keygen_bits:{key_size}"
        ], check=True)

        print(f"[+] Private key saved to: {private_key_path}")

        # Extract public key
        subprocess.run([
            OPENSSL_PATH, "rsa",
            "-pubout",
            "-in", private_key_path,
            "-out", public_key_path
        ], check=True)

        print(f"[+] Public key saved to: {public_key_path}")

    except subprocess.CalledProcessError as e:
        print("[!] Error occurred during key generation:", e)

if __name__ == "__main__":
    generate_rsa_keys()
