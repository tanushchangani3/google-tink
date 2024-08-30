import tink
from tink import aead
from tink import secret_key_access
import base64

aead.register()

def encrypt(text, key):
	key_bytes = base64.b64decode(key)
	key_string = key_bytes.decode('utf-8')
	print("key_string is:", key_string)

	keyset_handle = tink.json_proto_keyset_format.parse(key_string, secret_key_access.TOKEN)
	primitive = keyset_handle.primitive(aead.Aead)

	encrypted_bytes = primitive.encrypt(text.encode('utf-8'), key_bytes)
	return base64.b64encode(encrypted_bytes).decode('utf-8')

def decrypt(encrypted_text, key):
    key_bytes = base64.b64decode(key)
    key_string = key_bytes.decode('utf-8')
    keyset_handle = tink.json_proto_keyset_format.parse(key_string, secret_key_access.TOKEN)
    primitive = keyset_handle.primitive(aead.Aead)

    encrypted_bytes = base64.b64decode(encrypted_text.encode('utf-8'))
    decrypted_bytes = primitive.decrypt(encrypted_bytes, key_bytes)
    return decrypted_bytes.decode('utf-8')