import os
import csv

filename = "contacts.csv"

if not os.path.exists(filename):
    with open(filename , "w" , newline = "" , encoding = "utf-8") as f:
        write = csv.writer(f)
        write.writerow(["name" , "phone" , "email"])

def add_contact():
    name = input("name: ").strip()
    phone = input("phone: ").strip()
    email = input("email: ").strip()

    with open(filename, "r" , encoding = "utf-8") as f:
        rows = csv.DictReader(f)

        for row in rows:
            if row["name"].lower() == name.lower():
                print("sorry! can't add duplicates!")
                return
            
    with open(filename , "a" , encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name , phone , email])
        print("contact added successfully!")

def view_contacts():

    with open(filename , "r" ,encoding = "utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

        if len(rows) < 1:
            print("no contacts are found!")
            return
        
        print(f"\t\t{len(rows)} contacts\n")
    
        for row in rows[1:]:
            print(f"{row[0]} : {row[1]} : {row[2]}")

        print()

def search_contact():
    search = input("enter the name of the contact you want to search: ").strip().lower()
    found = False

    with open(filename , "r" , encoding = "utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if search in row["name"].lower():
                print(f"{row['phone']} : {row['email']}")
                found = True

    if found == False:
        print("no contact found!")

def delete_contact():
    delete = input("enter the name of the contact that you want to delete: ")
    found = False

    with open(filename , "r" , encoding = "utf-8") as f:
        reader = csv.DictReader(f)
        contacts = list(reader)

    new_contacts = []

    for row in contacts:
        if row['name'].lower() != delete.lower():
            new_contacts.append(row)
        else:
            found = True

    if found == False:
        print("no such contact found!")
    else:
        with open(filename , "r" , encoding = "utf-8") as f:
            writer = csv.DictWriter(f , fieldnames= ['name' , 'phone' , 'email']) #creates a dictionary with parameters with name , phone , email
            writer.writeheader() #this will write name , phone and email as header(on top)
            write.writerows(new_contacts) #this will finally fill the data

            print("contact deleted")

def update_contact():
    update = input("enter the name of contact you want to update: ")
    found = False

    with open(filename , "r" , encoding = "utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if update.lower() == reader['name'].lower():
                found = True

    if found == False:
        print("no such contact found!")
    else:
        print("1->update email id")
        print("2->update phone number")

        choice = int(input("enter your choice: "))

        if choice == 1:
            new_email = input("enter the new email: ")

            with open(filename , "r" , encoding = "utf-8") as f:
                reader = csv.DictReader(f)

                for rows in reader:
                    if rows['name'].lower() == update:
                        rows['email'] = new_email
                        break

                print("email updated successfully!")

        elif choice == 2:
            new_phone = input("enter the new email: ")

            with open(filename , "r" , encoding = "utf-8") as f:
                reader = csv.DictReader(f)

                for rows in reader:
                    if rows['name'].lower() == update:
                        rows['phone'] = new_phone
                        break

                print("phone number updated successfully")

        else:
            print("invalid choice!")
        
# def main():
    

# if __name__ == "__main__": #defining the starting point
#     main()

while True:
    print("Contact Book")
    print("1. Add contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = int(input("enter you choice(1-4): "))

    if choice == 1:
        add_contact()
    elif choice == 2:
        view_contacts()
    elif choice == 3:
        search_contact()
    elif choice == 4:
        break
    else:
        print("invalid choice of number!")
        


