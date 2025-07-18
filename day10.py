#friendship level calculator 

def score(name1 , name2):
    name1 , name2 = name1.lower() , name2.lower()
    score = 0

    common_letters = (set(name1) & set(name2)) #comparing all letters
    score += len(common_letters) * 10
    
    vowels = set('aeiou')

    common_vowels = common_letters & vowels
    score += len(common_vowels) * 10

    #special friendship
    if name1[0] == name2[0] and name1[len(name1)-1] == name2[len(name2)-1]:
        score += 20

    return min(score , 100)



name1 = input("enter 1st friend's name: ")
name2 = input("enter 2nd friend's name: ")

if name1.lower() == name2.lower():
    print("Both names can't be same!")
    
else:
    final_score = score(name1, name2)

    border = "*" * 100

    print(border)
    print(f"\t\t\tFriendship score of {name1} and {name2}: {final_score}")

    if final_score>80 :
        print("\n\t\t\t\tMade for each other!\n")
    elif final_score > 50:
        print("\n\t\t\t\tGreat Friendship! Keep it up!\n")
    elif final_score > 30:
        print("\n\t\t\t\tMore gelling required!\n")
    else:
        print("\n\t\t\t\tMaybe opposites attract!\n")

    print(border)


