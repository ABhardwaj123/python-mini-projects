# modified intro generator
import textwrap 

name = input("name: ")
profession = input("profession: ")
passion = input("your passion in one line: ")
emoji = input("your favourite emoji: ")
handle = input("your social media handle: ")

print("\nWe have 3 styles available to display your intro\n")
print("You can choose your style\n")
print("1. simple lines")
print("2. fire")
print("3. emoji sandwich")

style = int(input("enter you preferred style(1,2,3): "))

def generate_bio(style):
    if style == 1: #simple lines
       return f"{emoji} {name} \n {profession} \n 🦾 {passion} \n {handle}"
    elif style == 2: #fire
        return f"{emoji} {name} \n {profession} 🔥\n {passion} 🔥\n {handle}🔥"
    elif style == 3: #emoji sandwich
        return f"{emoji * 3} \n {name} \n {profession} \n {passion} \n {handle} {emoji * 3}"
    else:
        return "invalid choice!"
    
data = generate_bio(style)

print("your new bio: \n")

print("*" * 50)
print(textwrap.dedent(data))
print("*" * 50)


print("do you want to save your data in a text file?")
choice = input(print("enter yes or no: ")).lower()

if choice == "yes":
    file_name = f"{name.lower()}_bio.txt"

    with open(file_name , "w" , encoding = "utf-8") as f:
        f.write(data)

    print("file saved")
    

