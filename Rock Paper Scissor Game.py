Rock=  """ 
     ______
____/     ___)
        (______)
        (_____)
___     (____)
   \___ (___)
"""
paper="""
     ________
___/     ____)___
           ______)
           _____)
____      ____)
    \_______)

"""
Scissiors="""
     ________
___/     ____)___
             ____)
           __________)
____      (___)
    \_____(__)

"""

game_images=[Rock,paper,Scissiors]
import random
user_choice =int(input("Enter your Choice:Type 0 for Rock,1 for paper ,2 for Scissors"))
if user_choice>=3  or user_choice< 0:
    print("You have entered invalid number,You lose.")
else:
    print(game_images[user_choice])
    computer_choice=random.randint(0,2)
    print("computer_choice")
    print(game_images[computer_choice])
    print(computer_choice)
    if computer_choice == user_choice:
        print("It's a Draw")
    elif computer_choice == 0 and  user_choice == 2:
        print("You lose")
    elif computer_choice == 2 and  user_choice ==0 :
        print("You Win")
    elif computer_choice > user_choice:  #2>0
        print("You lose")
    elif computer_choice < user_choice:  #0>2
        print("You Win")


    
