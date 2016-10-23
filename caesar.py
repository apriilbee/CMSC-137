print("Caesar Cipher")
message = raw_input("Enter message: ")
operation = int(raw_input("Press 0 for encode and 1 for decode: "))
while (operation!= 0 and operation!=1):
    operation = int(raw_input("Press 0 for encode and 1 for decode: "))
key_input = raw_input("Enter offset: ")
if(key_input.isdigit()):
    key = int(key_input)
else:
    key = len(key_input)

# a-z: 97 - 122
# 0-9: 48 - 57
# A-Z: 65 - 90

def encrypt():
    encrypted = ""
    for ch in message:
        tmp = ord(ch) + key
        if (ch == " "):
            encrypted += ch
        elif(ch.islower() and tmp > 122):
            encrypted += chr(47 + (key - (122 - ord(ch))))
        elif(ch.isupper() and tmp > 90):
            encrypted += chr(96 + (key - (90 - ord(ch))))
        elif(ch.isdigit() and tmp > 57):
            encrypted += chr(64 + (key - (57 - ord(ch))))
        else:
            encrypted += chr(tmp);
    print(encrypted)

def decrypt():
    decrypted = ""
    for ch in message:
        tmp = ord(ch) - key
        if(ch == " "):
            decrypted += ch
        elif(ch.islower() and tmp < 97):
            decrypted += chr(91 - (key - (ord(ch) - 97)))
        elif(ch.isupper() and tmp < 65):
            decrypted += chr(58 - (key - (ord(ch) - 65)))
        elif(ch.isdigit() and tmp < 48):
            decrypted += chr(123 - (key - (ord(ch) - 48)))
        else:
            decrypted += chr(tmp);
    print(decrypted)

encrypt() if operation==0 else decrypt();
