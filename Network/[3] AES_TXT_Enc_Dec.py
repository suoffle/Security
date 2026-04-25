from Crypto.Cipher import AES
from Crypto.Util import Counter
import os, struct

def decrypt_file(key, filename):
    
    ctr=Counter.new(128)
    chunk_size = 1024
	
    with open(filename, 'rb') as infile:
        
        origsize = struct.unpack('<I', infile.read(struct.calcsize('I')))[0]
        decryptor=AES.new(key, AES.MODE_CTR, counter=ctr)
        
        result=b''
        while 1:
            chunk = infile.read(chunk_size)

            if len(chunk)==0:
                break
            result+=decryptor.decrypt(chunk) 
        result=result[:origsize]     
    print(result.decode("ascii"))


decrypt_file(b"ABCDEF0123456789", "enc2.txt");
