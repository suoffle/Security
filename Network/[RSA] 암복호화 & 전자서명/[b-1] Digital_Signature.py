from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA
import base64

#make key pair
key=RSA.generate(2048)
pubkey=key.publickey().export_key(format='DER')

#write public key to file
with open("public.der","wb") as f:
    f.write(pubkey)

#read file
content=b""
with open("1.txt","rb") as f:
    content=f.read()

#signature
h=SHA.new()
h.update(content)

signer=PKCS1_PSS.new(key)
sig=signer.sign(h)

#write message(content) and encoded signature to file
with open("sig.txt","wb") as f:
    f.write(content+b"---signature---\n")
    f.write(base64.b64encode(sig))
