# Digital image signing with RSA in Python. Cybersecurity final project

I this project I implemented a simple and effective way to digitally sign and verify PNG images using RSA-4096 cryptography. The digital signature is embedded invisibly** into the image metadata. Also, the full quality and visual appearence of the image remain the same after signature.

---

## Project steps

- Generate a 4096-bit RSA key pair  
- Digitally sign an image using the private RSA key  
- Embed the signature in the image metadata (`TEXT` chunk in PNG)  
- Verify the image using the public RSA key  
- Keep the image visually unchanged and openable in standard viewers

---

## Potential Applications

Ponential business applications include:

- Watermarking and authenticity verification of digital images
- Secure document or certificate distribution
- Tamper detection for sensitive media
- Copyright and intellectual property protection

---

## Approach

1. Key Generation:
   - I used OpenSSL to generate `private_key.pem` and `public_key.pem` (4096-bit RSA)

2. Image signing:
   - Uses `Pillow` to load the image
   - Hashes the raw pixel data (not metadata, it is crucial because at first I was hashing metadata and it was incorrect)
   - Signs the hash using `pycryptodome` and embeds the signature into the PNG metadata (`Signature` field)

3. Image verification:
   - Loads the image and reads the `Signature` from metadata
   - Recalculates the hash from raw pixel data
   - Verifies the signature using the public key

---

## Installing dependencies

Install all the needed libraries using pip:

```bash
pip install -r requirements.txt
