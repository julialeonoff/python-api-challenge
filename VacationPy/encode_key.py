import base64

#Encode the key and write it to a file:
k = input("What is they developer key?")
with open('config.py','wb') as outf:
    outf.write(base64.b64encode(k.encode('utf8')))


#Use the following to retrieve the decoded key:
def get_key(keyfile='config.py'):
    with open(keyfile,'rb') as inf:
        k = base64.b64decode(inf.read())
        inf.close()
    return k.decode('utf8')

#print(get_key())