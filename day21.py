#cryptography using fernet system
import json
import os
from cryptography.fernet import Fernet
from datetime import datetime

vault_file = "notes.json"
key_file = "vault.key"

def load_or_create_key():
    if not os.path.exists(key_file):
        key = Fernet.generate_key()

        with open(key_file , "wb") as f: # wb -> write in binary
            f.write(key)

    else:
        with open(key_file , "rb") as f:
            key = f.read()

    return Fernet(key)

fernet = load_or_create_key()


def load_vault():
    if not os.path.exists(vault_file):
        return []
    
    with open(vault_file , 'r' , encoding ="utf-8") as f:
        return json.load(f)
    
    
#saving the upper json dump
def save_vault(data):
    with open(vault_file , 'w' , encoding="utf-8") as f:
        json.dump(data, f , indent = 2)

def add_note():
    title = input("enter your note title: ").strip()
    body = input("enter your note: ").strip()

    encrypted_data = fernet.encrypt(body.encode()).decode()
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    data = load_vault()

    data.append({
        "title": title,
        "content": encrypted_data,
        "time": timestamp
    })

    save_vault(data)
    print("data saved!")

def list_notes():
    data = load_vault()

    if not data:
        print("no notes created!")
        return
    
    for i , note in enumerate(data , 1):
        print(f"{i}. {note['title']} {note['timestamp']}")

def view_notes():
    list_notes()

    try:
        choice = int(input("enter number number that you want to view: ")) - 1
        data = load_vault()

        if 0 <= choice <= len(data):
            encrypted = data[choice]["body"]
            decrypted = fernet.decrypt(encrypted.encode()).decode()

            print(f"\n {data[choice]['title']} - {data[choice]['timestamp']} \n {decrypted}")
        
        else:
            print("invalid choice!")

    except:
        print("invalid input")


def search_notes():
    keyword = input("enter the keyword for note search: ").strip().lower()
    data = load_vault()

    #writing array comprehensions because multiple nodes can be there
    matches = [note for note in data if keyword in note['title'].lower()]

    if not matches:
        print("no matches found!")
    else:
        for note in matches:
            print(f"{note['title']} -> {note['timestamp']}\n")



def main():   
    while True:
        print("\nNotes Locker")
        print("1. Add Note")
        print("2. List Notes")
        print("3. View Note")
        print("4. Search Notes")
        print("5. Exit")

        option = int(input("enter your choice: "))

        match option:
            case 1:
                add_note()
            case 2:
                list_notes()
            case 3:
                view_notes()
            case 4:
                search_notes()
            case 5:
                break
            case _:
                print("invalid choice")


if __name__ == "__main__":
    main()
