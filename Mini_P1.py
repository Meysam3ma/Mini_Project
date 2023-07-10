import random
random_number =int(random.randrange(1,100))
print(random_number)
user_number = int(input("enter you number"))
for x in range(6):
    if random_number < user_number :
                print(" enter low number")
                user_number =  int(input(" try agin"))
    elif random_number > user_number :
                print("enter hight number")
                user_number =  int(input(" try agin"))
    elif random_number == user_number :
            print(" you are winner")
else:
        print("you are loser")
    
    