#timer

import time

while True:
    try:
        seconds = int(input("enter seconds for timer: "))

        if seconds < 1:
            print("timer entered should be above 1!")
            continue

        break

    except ValueError:
        print("invalid time!")

print("Timer started")

for time_left in range(seconds , -1 , -1): # for reverse loop
    mins , secs = divmod(time_left , 60) #divmod is used to divide and do mod of "time_left" to get the entered time(which was in seconds) in mins and seconds
    time_format = f"{mins:02} : {secs:02}" #mins:02 means that mins till 2 places
    print(f"Time left : {time_format} " , end = "\r") #end = "\r" will keep updating the answer in same line, overwrites previous output
    time.sleep(1) #so that loop runs after every 1 sec

print("\ntime over!")
print("\a")



