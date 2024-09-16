#what do you choose? Type 0 for rock, 1 for paper or 2 for Scissors
#computer will choose randomly then compare both and print who will win
import random
rock='''
     __________
____'  ________)
      (________)
      (_________)
      (_________)
_____.(______) 
'''
scissors='''
      
_____'  ______________        
      _________)_______)
           ___________)
          ________________)
          (__________)
______.
     _____(______-)         
'''
paper='''
   -----------
   ----------
   ---------
   -------
   ----
'''
#to include images
game_images=[rock,paper,scissors]
user_choice=int(input("what do you choose? Type 0 for rock, 1 for paper or 2 for Scissors"))
print(game_images[user_choice])
computer_choice=random.randint(0,2)
print(game_images[computer_choice])
print(f"computers choice {computer_choice}")

##comparing
if user_choice>=3 or user_choice<0:
    
    print("you types an invalid number so You lose")

elif user_choice==0 and computer_choice==2:
    print("You wins")
elif computer_choice==0 and user_choice==2:
    print("you lose")
elif computer_choice>user_choice:
    print("you loose")
elif user_choice>computer_choice:
    print("you win")
elif computer_choice==user_choice:
    print("its a draw!")
    


