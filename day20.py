#credential manager
import base64 #necessary to use .encode()
import os

vault_file = "vault.txt"

def encode(text):
    return base64.b64encode(text.encode()).decode() #the text.encode() encodes text to binary form
    #the .decode() then is used to remove the b form(binary form) of the string
    #b64encode is used for the encoding

def decode(text):
    return base64.b64decode(text.encode()).decode()

def password_strength(password):
    length = len(password)
    uppercase = any(c.isupper() for c in password)
    lowercase = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special_char = any(c in "!@#$%&*()" for c in password)

    score = sum([length >=8 , uppercase , lowercase , digit , special_char])

    return ["very weak" , "weak" , "medium" ,"strong" , "very strong"][min(score , 4)]

def add_credentials():
    website = input("website: ")
    username = input("username: ")
    password = input("password: ")

    strength = password_strength(password)

    data = f"{website} -> {username} -> {password}"
    encoded_data = encode(data)

    with open(vault_file, 'a', encoding = "utf-8") as f:
        f.write(encoded_data)
        f.write("\n")

    print("data saved!")

def view_credentials():
    if not os.path.exists(vault_file):
        print("vault file not found!")
        return
    
    with open(vault_file, 'r' , encoding = "utf-8") as f:
        for line in f:
            decoded = decode(line.strip())
            website , username , password = decoded.split("->")

            print(f"{website} -> {username} -> {password}")

def update_password():
    if not os.path.exists(vault_file):
        print("Vault file not found!")
        return
    
    search = input("enter the username for which you want to update password: ")
    new_pass = input("enter new password: ")

    updated_line = []
    update = False

    with open(vault_file , 'r', encoding = "utf-8") as f:
        for line in f:
            decoded = decode(line.strip())
            website , username , password = decoded.split("->")

            if username.lower() == search.lower():
                password = new_pass
                update = True

                print("password updated successfully!")
                
            updated_line = encode(f"{website} -> {username} -> {password}")
            updated_line.append(updated_line)

            if not update:
                print(f"{search} not found in vault file!")
            else:
                with open(vault_file , "w" , encoding = "utf-8") as f:
                    for line in updated_line:
                        f.write(line)
                        f.write("\n")
            
        print(f"{search} not found in vault file!") 


def main():
    while True:
        print("1.Add credentials")
        print("2. View credentials")
        print("3. Update password")
        print("4. Exit")

        choice = int(input("enter your choice: "))

        if choice == 1:
            add_credentials()
        elif choice == 2:
            view_credentials()
        elif choice == 3:
            update_password()
        elif choice == 4:
            break
        else:
            print("invalid choice")

if __name__ == "__main__":
    main()