import getpass
attempt = 3
database = {"bala": "123456", "kumar": "654321"}
username = input("Enter Your Username : ")

for i in database.keys():
    
    if username == i:
        password = getpass.getpass("Enter Your Password : ")
        
        if password == database.get(i):
            print("Verified")
            break;
        else:
                while(attempt!=0):
                    password = getpass.getpass("Enter Your Password Again : ")
                    attempt = attempt-1
                    if password == database.get(i):
                        print("Verified")
                    else:
                        print("INCORRECT PASSWORD YOU HAVE ONLY {} ATTEMPTS".format(attempt))
                print("!AUTHENTICATION FAILED")
                break;   
            
    else:
        print("incorrect username")
        break;
