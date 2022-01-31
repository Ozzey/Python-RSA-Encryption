
from functions import encryptor, decryptor, creator

print('''__      __      _
\ \    / / ___ | | __  ___  _ __   ___
 \ \/\/ / / -_)| |/ _|/ _ \| '  \ / -_)
  \_/\_/  \___||_|\__|\___/|_|_|_|\___|
''')

a=3
while(a>0):
    print("Press\n")
    print("1.For generating Encryption Keys\n")
    print("2.For Encrypting\n")
    print("3.For Decrypting \n")
    print("4.To exit")
    print("")
    command = input("Enter : ")


    if command=='1':
        creator()
        a=a-1
        print("")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("Keys Generated!")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    elif command== '2':
        try:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            encryptor()
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("Encryption Successful!")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            a=a-1

        except:
            print("Please create the keys first")

    elif command== '3':
        try:
            print("Successfully decrypted!")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            decryptor()
            a=a-1

        except:
            print("Please create the keys first")

    elif command=="4":
        quit()

    else:
        print("")
        print("Please enter a valid command")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
