from AEDS.encryption import encrypt
@pytest.fixture(scope="session")
def encryption_message():
    return "Example Text String"
    
class TestEncryption:
    def test_encrypt_message(self, encryption_message):
