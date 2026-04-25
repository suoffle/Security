from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA
import base64

#get public key
with open("public.der","rb") as f:
    readkey=f.read()
    pubkey=RSA.import_key(readkey)

#get original text
with open("1.txt","rb") as f:
    content=f.read()

#get signature
with open("sig.txt","rb") as f:
    msg,sig=f.read().split(b"---signature---\n")
    sig=base64.b64decode(sig)

#hash original message(content)
h=SHA.new()
h.update(content)

#check result
verifier=PKCS1_PSS.new(pubkey)
if(verifier.verify(h,sig)):
    print("verified")
else:
    print("not verified")
