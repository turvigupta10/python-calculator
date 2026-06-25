import random
user_choice=int(input("enter your guess between 1-50"))
comp_choice= random.randint(1,50)
attempts=1

print(f"user choice = {user_choice}")

while user_choice != comp_choice and attempts!=7:

 if user_choice > comp_choice:
    print("go lower")
 elif user_choice < comp_choice:
    print("go higher") 
 attempts+=1
 user_choice=int(input("enter your guess"))
 print(f"number of attempts left : {attempts-7} ")

print("you gussed it!")
print(f"you gussed it in {attempts}")




