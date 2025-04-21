from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from PIL import Image, PngImagePlugin
import base64

def sign_image(image_path, private_key_path, output_path):
    with open(image_path, "rb") as f:
        image_data = f.read()

    img = Image.open(image_path)
    pixel_data = img.tobytes()
    hash_obj = SHA256.new(pixel_data)



    with open(private_key_path, "rb") as f:
        private_key = RSA.import_key(f.read())

    signature = pkcs1_15.new(private_key).sign(hash_obj)
    signature_b64 = base64.b64encode(signature).decode()

    img = Image.open(image_path)
    meta = PngImagePlugin.PngInfo()
    meta.add_text("Signature", signature_b64)

    img.save(output_path, "PNG", pnginfo=meta)

    print(f"[+] Image signed and saved as {output_path}")



if __name__ == "__main__":
    sign_image(
        image_path="dog.png",
        private_key_path="private_key.pem",
        output_path="signed_image.png"
    )
