from Crypto.Hash import SHA512

for i in range(0,2**24):
    obj=SHA512.new()
    obj.update(str(i).encode('ascii'))
    hash_digest=obj.digest()
    if(hash_digest[:3]==b'\x00\x00\x00'):
            print(i)
