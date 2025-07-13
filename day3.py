#bill splitter

def get_float(total_amount):
    while True:
        try:
            return float(input(total_amount)) 
        except ValueError:
            print("enter a valid number: ")

people = int(input("number of people: "))

names = []


for i in range(1,people+1):
    name = input(f"enter name of person #{i}: ").strip()
    names.append(name)

total_amount = get_float("enter the bill amount: ")

split = round(total_amount / people,2) #this will round the final answer to two decimal places

print("\nbill split is as follows: \n")

for name in names:
    print(f"{name} has to pay {split}")

print("\nThank You!\n")

