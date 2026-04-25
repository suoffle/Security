from Crypto.Cipher import AES
import os, random, struct

def decrypt_file(key, filename):
	
    chunk_size = 1024
	
    with open(filename, 'rb') as infile:
        
        iv = b"Netsec@Soongsil."
        origsize = struct.unpack('<I', infile.read(struct.calcsize('I')))[0]
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        result=b""	 
        while 1:
            chunk = infile.read(chunk_size)

            if len(chunk)==0:
                break
            result+=decryptor.decrypt(chunk)

        result=result[:origsize] 
        print(result.decode('ascii'))


decrypt_file(b"ABCDEF0123456789", 'enc1.txt');
