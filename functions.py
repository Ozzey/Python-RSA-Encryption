import rsa
from cryptography.fernet import Fernet

def creator():
# create the symmetric key
    key = Fernet.generate_key()

    # write the symmetric key to a file
    k = open('keys/symmetric.key','wb')
    k.write(key)
    k.close()

    # create the pub & private keys
    (pubkey,privkey)=rsa.newkeys(2048)

    # write the public key to a file
    pukey = open('keys/publickey.key','wb')
    pukey.write(pubkey.save_pkcs1('PEM'))
    pukey.close()

    # write the private key to a file
    prkey = open('keys/privkey.key','wb')
    prkey.write(privkey.save_pkcs1('PEM'))
    prkey.close()


def decryptor():
    prkey = open('keys/privkey.key','rb')
    pkey = prkey.read()
    private_key = rsa.PrivateKey.load_pkcs1(pkey)

    e = open('keys/encrypted_key','rb')
    ekey = e.read()

    dpubkey = rsa.decrypt(ekey,private_key)

    cipher = Fernet(dpubkey)

    encrypted_data = open('mysecretdata','rb')
    edata = encrypted_data.read()
    encrypted_data.close()

    decrypted_data = cipher.decrypt(edata)
    og = open('mysecretdata','wb')
    og.write(decrypted_data)

    print(decrypted_data.decode())


def encryptor():
    # open the symmetric key file
    skey = open('keys/symmetric.key','rb')
    key = skey.read()

    # create the cipher
    cipher = Fernet(key)

    # open file for encrypting

    myfile = open('mysecretdata','rb')
    myfiledata= myfile.read()
    myfile.close()
    # encrypt the data
    encrypted_data = cipher.encrypt(myfiledata)
    edata = open('mysecretdata','wb')
    edata.write(encrypted_data)

    print(encrypted_data)

    # open the public key file
    pkey = open('keys/publickey.key','rb')
    pkdata = pkey.read()

    # load the file
    pubkey = rsa.PublicKey.load_pkcs1(pkdata)

    # encrypt the symmetric key file with the public key
    encrypted_key = rsa.encrypt(key,pubkey)

    ekey = open('keys/encrypted_key','wb')
    ekey.write(encrypted_key)

    print(encrypted_key)


#encrypt_func()
