# self intro script generator

import datetime

name = input("name: ")
age = int(input("age: "))
city = input("place where you reside: ")
profession = input("profession: ")
hobby = input("hobby: ")

star_design = "*" * 100



intro_script = (f"Hello! My name is {name}. I'm {age} years old and I live in {city}.\n"
				f"My profession is {profession} and coming to my hobbies, I really enjoy {hobby} in my free time")

print("\n" + star_design + "\n" + intro_script + "\n")

current_date = datetime.date.today().isoformat()

print("date on which data is displayed: " + current_date + "\n" + star_design)


