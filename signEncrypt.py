import base64
import math
import binascii

#Key is in base64
#0 encrypt, 1 decrypt
def enanddecrypt(mode, input, key):

    #Gets the individual b64 keys and turns encodes them as bytes
    enK = key[0].encode()
    enN = key[1].encode()

    #Turns the b64 keys into ints
    k = int.from_bytes(base64.b64decode(enK), "little")
    n = int.from_bytes(base64.b64decode(enN), "little")
    m = str(input)

    if mode == 0:
        #Encodes the message into byte form
        enM = m.encode()
        #Turns the message into an int
        intM = int.from_bytes(enM, "little")
        #Creates the cipher text
        cipherT = pow(intM, k, n)
        #Turns the cipher text into base 64
        cipherT64 = base64.b64encode(cipherT.to_bytes(math.ceil(cipherT.bit_length()/8), "little"))
        #Removes the byte notation from the base 64 cipher text
        toBeWritten = cipherT64.decode()
    elif mode == 1:
        try:
            #Encodes the encrypted message into byte form
            enM = m.encode()
            #Turns the encrypted message into the int form cipher text
            cipherT = int.from_bytes(base64.b64decode(enM), "little")
            #Gets the int form of the plain text
            intM = pow(cipherT, k, n)
            #Gets the byte form of the plain text
            enM = intM.to_bytes(math.ceil(intM.bit_length()/8), "little")
            #Gets the string form from the byte form
            toBeWritten = enM.decode()
        except binascii.Error:
            print("Incorrect Encryption")
            toBeWritten = None
    return toBeWritten
'''
#Input is 0, 1, 2, 3, signalling: sign with public, encrypt with private, decrypt with private, decrypt with public
def enanddecrypt(mode, puKeyFile, prKeyFile, input)

    keys = []

    with open(puKeyFile, 'r') as puKey:
        keys.append(puKey.read())

    with open(prKeyFile, 'r') as prKey:
        keys.append(prKey.read())

    #Gets the individual b64 keys and turns encodes them as bytes
    public = keys[0].split(", ")
    enE = public[0].encode()
    enN = public[1].encode()
    private = keys[1].split(", ")
    enD = private[0].encode()

    enE =

    #Turns the b64 keys into ints
    e = int.from_bytes(base64.b64decode(enE), "little")
    d = int.from_bytes(base64.b64decode(enD), "little")
    n = int.from_bytes(base64.b64decode(enN), "little")

    if mode == 0 or mode == 1:
        #Encodes the message into byte form
        enM = m.encode()
        #Turns the message into an int
        intM = int.from_bytes(enM, "little")
        dMode = ""
        #Creates the cipher text
        if mode == 0:
            cipherT = pow(intM, d, n)
        else:
            cipherT = pow(intM, e, n)
        #Turns the cipher text into base 64
        cipherT64 = base64.b64encode(cipherT.to_bytes(math.ceil(cipherT.bit_length()/8), "little"))
        #Removes the byte notation from the base 64 cipher text
        toBeWritten = cipherT64.decode()
    elif mode == 2 or mode == 3:
        try:
            #Encodes the encrypted message into byte form
            enM = m.encode()
            #Turns the encrypted message into the int form cipher text
            cipherT = int.from_bytes(base64.b64decode(enM), "little")
            #Gets the int form of the plain text
            if mode == 2:
                intM = pow(cipherT, e, n)
            else:
                intM = pow(cipherT, d, n)
            #Gets the byte form of the plain text
            enM = intM.to_bytes(math.ceil(intM.bit_length()/8), "little")
            #Gets the string form from the byte form
            toBeWritten = enM.decode()
        except binascii.Error:
            print("Incorrect Encryption")
            toBeWritten = None
    return toBeWritten
'''
