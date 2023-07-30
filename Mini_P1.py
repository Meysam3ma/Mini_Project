#  Number Guessing Game

# import random
# random_number =int(random.randrange(1,100))
# print(random_number)
# user_number = int(input("enter you number"))
# for x in range(6):
#     if random_number < user_number :
#                 print(" enter low number")
#                 user_number =  int(input(" try agin"))
#     elif random_number > user_number :
#                 print("enter hight number")
#                 user_number =  int(input(" try agin"))
#     elif random_number == user_number :
#             print(" you are winner")
# else:
#         print("you are loser")
    
    


# Word Count Tool 

from collections import Counter 
with open('text1.txt','r') as user_text :
    list_a=list(user_text.readlines())

for i in list_a:
    print (i.split())

len_list =  len(list_a)
counter = Counter(list_a)
print(counter , len_list)
sorted_counter = sorted(counter.items(), key=lambda x : x[1] )

for i in sorted_counter:
    print(i[0] , i[1])
    