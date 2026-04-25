# AES pycrypto package
from Crypto.Cipher import AES

while 1:
    # Fill with spaces the user until 32 characters
    str=input("\nmessage: ")
    message=str.encode('ascii')
    #print ("message length: ", len(message) )

    # key: 16 bytes
    encrypt_AES = AES.new(b'secret-key-01234', AES.MODE_CFB, b'IV-0123456789ABC')
    
    ciphertext = encrypt_AES.encrypt(message)
    print("Cipher text: " , ciphertext)

    # key: same as encrypt
    decrypt_AES = AES.new(b'secret-key-01234', AES.MODE_CFB, b'IV-0123456789ABC')
    message_decrypted =  decrypt_AES.decrypt(ciphertext)

    print("Decrypted text: ",  message_decrypted.decode('ascii'))
