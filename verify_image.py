from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from PIL import Image
import base64

def verify_image_signature(image_path, public_key_path):
    img = Image.open(image_path)
    metadata = img.info

    if "Signature" not in metadata:
        print("No signature.")
        return False

    signature_b64 = metadata["Signature"]
    signature = base64.b64decode(signature_b64)

    img = Image.open(image_path)
    pixel_data = img.tobytes()
    hash_obj = SHA256.new(pixel_data)

    with open(public_key_path, "rb") as f:
        public_key = RSA.import_key(f.read())

    try:
        pkcs1_15.new(public_key).verify(hash_obj, signature)
        print("Nice - signature is valid.")
        return True
    except (ValueError, TypeError):
        print("Invalid signature! The image may have been tampered with.")
        return False

if __name__ == "__main__":
    verify_image_signature(
        image_path="signed_image.png",
        public_key_path="public_key.pem"
    )
