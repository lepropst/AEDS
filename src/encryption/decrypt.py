import nacl.secret
from nacl.exceptions import CryptoError

def decrypt_message(key, ciphertext):
    box = nacl.secret.SecretBox(key)
    try:
        decrypted = box.decrypt(bytes.fromhex(ciphertext))
        return decrypted.decode()
    except CryptoError:
        return None