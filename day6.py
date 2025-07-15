#journal logger
import datetime

learning = input("what did you learn today? \n")

choice = input("anything special that you would like to record(yes/no): ").lower()

if choice == "yes":
    special = input("what special thing happened today? \n")

rating = int(input("how productive was your day on a scale of 1-10? \n"))

end = "*" * 100

current_time = datetime.datetime.now()
current_time.strftime("%d/%m/%Y : %H:%M:%S")
#print(current_time)

entry = f"entry day-time details: {current_time}\n\n"
entry += learning + "\n" + f"special thing that happened: {special}" + "\n" 
entry += f"Rating of productivity : {rating}\n" + end


with open("journal.txt" , "a" , encoding = "utf-8") as f:
    f.write(entry)

print("today's journaling done!")