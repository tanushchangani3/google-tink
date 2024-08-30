import sys
sys.path.append('/home/pyuser/app/dist-packages/')
import os
from flask import Flask
from crypto import encrypt, decrypt

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def greeting():
    unwrapped_dek = 'XX'
    encrypted_value = encrypt("example", unwrapped_dek)
    print("Encrypted value:", encrypted_value)
    decrypted_value = decrypt(encrypted_value, unwrapped_dek)
    print("Decrypted value:", decrypted_value)
    return 'Google Tink Cryptography'

if __name__ == '__main__':
    app.run('0.0.0.0','8080')