import nacl.secret
import nacl.utils
from nacl.encoding import HexEncoder
from nacl.exceptions import CryptoError
from utilities import generate_key


def encrypt_message(key, message):
    box = nacl.secret.SecretBox(key)
    nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)
    try:
        encrypted = box.encrypt(message.encode(), nonce)
        return encrypted.ciphertext.hex()
    except CryptoError:
        return None
