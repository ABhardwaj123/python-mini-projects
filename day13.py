#student marks collector 

def student_data():
    data = {}

    while True:
        print("enter name or write nil to exit")
        name = input("name of the student: ").strip().lower()

        if name == 'nil':
            break
        
        if name in data:
            print("name already exists!")
            continue

        try:
            marks = float(input(f"enter marks of {name}"))

            if marks<0 or marks>100:
                raise ValueError()
            else:
                data[name] = marks

        except ValueError:
            print("invalid marks!")

    return data

def detailed_data(data):
    if not data:
        print("empty dataset!")

    marks = list(data.values())
    max_marks = max(marks)
    min_marks = min(marks)

    average_marks = sum(marks) / len(marks)

    studs_with_max_marks = [name for name, mark in data.items() if mark == max_marks]
    studs_with_min_marks = [name for name, mark in data.items() if mark == min_marks]

    print(f"maximum marks: {max_marks}")
    print(f"students who scored {max_marks} : {', '.join(studs_with_max_marks)}\n")

    print(f"minimum marks: {min_marks}")
    print(f"students who scored {min_marks} : {', '.join(studs_with_min_marks)}")

    print(f"average marks :{average_marks}")



def display_all_data(data):

    for name, score in data.items():
        print(f"{name} :{score}")


stud_dictionary = student_data()


detailed_data(stud_dictionary)
display_all_data(stud_dictionary)
