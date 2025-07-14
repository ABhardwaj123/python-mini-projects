# calculating the time alive for as many times you want

def calculate_time(age):
    #assuming each year has 365.25days

    days = age * 365.25
    hours = days * 24
    minutes = hours * 60

    return round(days) , round(hours) , round(minutes)



while True:
    try:
        age = float(input("enter your age in years: "))
        days , hours , minutes = calculate_time(age)

        #comma formatting
        formatted_days = format(days , ",")
        formatted_hours = format(hours , ",")
        formatted_minutes = format(minutes , ",")

        print(f"\nyou have lived {formatted_days} days")
        print(f"you have lived {formatted_hours} hours")
        print(f"you have lived {formatted_minutes} minutes\n")
        

        choice = input("would you like to try again(yes/no): ").lower()

        if choice != "yes":
            print("thanks for using this calculator")
            break

    except:
        print("proved a valid float value!\n")
