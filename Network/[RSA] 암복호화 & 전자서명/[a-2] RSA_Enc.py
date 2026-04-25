from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

#read file and get public key
with open("Alice_public.pem","rb") as f:
    pubkey=RSA.import_key(f.read())

#read message(content)
with open("1.txt","rb") as f:
    content=f.read()

#encrypt message(content) and wrtie to file
encryptor=PKCS1_OAEP.new(pubkey)
ciphertext=encryptor.encrypt(content)

with open("Enc.txt","wb") as f:
    f.write(str(len(content)).encode('ascii')+b'\n'+ciphertext)
