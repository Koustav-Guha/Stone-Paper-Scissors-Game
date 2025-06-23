import random

choices = [0, -1, 1]
print("\n-----------------------------------------")
print("|           Welcome to the              |")
print("|       Stone-Paper-Scissors Game!      |")
print("-----------------------------------------")

Your_score = 0
computer_score = 0

print("\nChoices are stone,paper,scissor... \n")
rounds = int(input("\nEnter the number of rounds you want to play : "))

for i in range(rounds):
    
    random.shuffle(choices)
    computer = random.choice(choices)
    
    you_str = input("Enter your choice: ").lower()
    
    youDict = {"stone": 1,
               "paper": -1,
               "scissor": 0}
    
    RevDict = {1: "stone"
               ,-1: "paper"
               ,0:"scissor"}

    you = youDict[you_str]

    print(f"\nComputer choose : {RevDict[computer]}\n")

    if(computer==you):
    
        print("It's a tie! Well played!")
        print("Try again!\n")
        
    else:
    
        if(computer == -1 and you == 1 ):
      
         print("The computer won the game! Better luck next time!\n")
         print("Try again!\n")
         computer_score += 1
         
        elif(computer == -1 and you == 0):
      
         print("Congratulations! You won the game!\n")
         
         Your_score += 1

        elif(computer == 1 and you == -1):
      
         print("Congratulations! You won the game!\n")
         
         Your_score += 1

        elif(computer == 1 and you == 0):
      
         print("The computer won the game! Better luck next time!\n")
         print("Try again!\n")
         computer_score += 1
         

        elif(computer == 0 and you == -1):
      
         print("The computer won the game! Better luck next time!\n")
         print("Try again!\n")
         computer_score += 1
         
        elif(computer == 0 and you == 1):
         
         print("Congratulations! You won the game!\n")
         
         Your_score += 1 

        else:
      
         print("something went wrong!!\n")
         print("Try again!\n")

print(f"\nFinal Score.... \nYou: {Your_score}\nComputer: {computer_score}\n")

if  (Your_score > computer_score):
    print("Congratulations! You won the game!\n")

elif (Your_score < computer_score):
    print("The computer won the game! Better luck next time!\n")

else:
    print("It's a tie! Well played!\n")