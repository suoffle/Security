from Crypto.PublicKey import RSA

keypair=RSA.generate(2048)
#passphrase
passphr="abcde"

#private key
prikey=keypair.export_key(passphrase=passphr)
with open("Alice_private.pem","wb") as f:
    f.write(prikey)

#public key
pubkey=keypair.publickey().export_key()
with open("Alice_public.pem","wb") as f:
    f.write(pubkey)

