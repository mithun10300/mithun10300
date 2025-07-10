import random
import string

def password_generator (length):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password= ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the password generator.")
    
    length = int (input("enter the length of password:"))
    try:
        if length < 4:
         print("password should be more than 4 characters.") 
        else:
            password= password_generator(length)
            print(f"generated password:{password}")
    except ValueError:
        print("invalid input.")
        
if __name__ == "__main__":
    main()
    
        
        
        
           

    
    