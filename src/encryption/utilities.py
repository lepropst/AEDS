def generate_key():
    return nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
