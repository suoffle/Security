from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

#get passphrase from user
passphr=input("Passphrase?: ")

#get private key
with open("Alice_private.pem","rb") as f:
    prikeyPEM=f.read()
    prikey=RSA.import_key(prikeyPEM,passphrase=passphr)

#read Enc.txt file and decrypt
ciphertext=b""
with open("Enc.txt","rb") as f:
    length=int(f.readline().decode('ascii'))
    #while len(ciphertext)<length:
    #	ciphertext+=f.readline()
    ciphertext=f.read(length)

decryptor=PKCS1_OAEP.new(prikey)
content=decryptor.decrypt(ciphertext)

print(content)
