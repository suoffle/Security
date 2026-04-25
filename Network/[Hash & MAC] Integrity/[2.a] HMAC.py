from Crypto.Hash import HMAC

#get password from user
key=input("Your key?: ")
h=HMAC.new(key.encode('ascii'))

msg=""

#get message(msg) from '2.txt' and update
with open('2.txt','r') as f:
	msg=f.read()
	h.update(msg.encode('ascii'))

#digest message(msg)
hmac=h.digest()
print("HMAC: "+str(hmac))

#write '2.txt' message and HMAC to 'H.txt'
with open('H.txt','w') as f:
        f.write(msg)
        f.write("HMAC:"+str(hmac)+"\n") #add "\n" to see answer clearly
