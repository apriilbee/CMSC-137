dictionary = []

def createList():
    asc = 97
    for i in range(0,26):
        dictionary.append(chr(asc))
        asc += 1

    asc = 48
    for i in range(0,10):
        dictionary.append(chr(asc))
        asc += 1

    asc = 65
    for i in range(0,26):
        dictionary.append(chr(asc))
        asc += 1

def encrypt():
    encrypted = ""
    for ch in message:
        if(ch == " "):
            encrypted += ch
            continue;

        tmp = dictionary.index(ch)+key
        if(tmp<=len(dictionary)):
            encrypted += dictionary[tmp]
        else:
            encrypted += dictionary[tmp % len(dictionary)]
    print(encrypted)

def decrypt():
    decrypted = ""
    for ch in message:
        if(ch == " "):
            decrypted += ch
            continue;

        tmp = dictionary.index(ch)-key
        if(tmp>=0):
            decrypted += dictionary[tmp]
        else:
            decrypted += dictionary[len(dictionary) + tmp]
    print(decrypted)

####

while True:
    createList()
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
    encrypt() if operation==0 else decrypt();

    print " "
    run_again = raw_input("Run Caesar Cipher again? yes or no \n").lower()
    if run_again != "yes":
        break;
    print " "
