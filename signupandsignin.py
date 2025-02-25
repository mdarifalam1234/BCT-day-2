L = []  
def signup():
    email = input("Enter the email: ")
    password = input("Enter the password: ")
    user = {"email": email, "password": password}
    L.append(user)  
    print("Signup successful!")

def signin():
    email = input("Enter the email: ")
    password = input("Enter the password: ")
    
    for user in L:
        if user["email"] == email and user["password"] == password:
            print("Signin successful!")
            return
    print("Invalid credentials. Please try again.")

signup()  
signin()  