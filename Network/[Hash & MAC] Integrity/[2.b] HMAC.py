from Crypto.Hash import HMAC

#get key from user
key=input("Your key?: ")
h=HMAC.new(key.encode('ascii')) 

HMAC1=""
msg=""

#get message(msg) and hmac(HMAC1) from file(f)
with open('H.txt','r') as f:
        line=f.readline()
        while line:
                if not line:
                        break

                elif line[0:4]=="HMAC":
                        HMAC1+=line[5:].strip()
                        break
                else:
                        msg+=line
                
                line=f.readline()	

#update and digest message(msg)
h.update(msg.encode('ascii'))
HMAC2=h.digest()

print("HMAC1: "+str(HMAC1))
print("HMAC2: "+str(HMAC2))

#check integrity
if HMAC1 == str(HMAC2) : 
	print ("OK")
else:
	print("NOK")

