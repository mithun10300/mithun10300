import random
print("welcome to rolling dice simulator.")

while(True):
  user_input= input("🎲Do you want to roll a dice(y/n):").lower()
 
  if user_input == "y":
    Roll_dice= random.randint(1,6)
  
    print(f"you got {Roll_dice}.")
    
    
  elif user_input == "n":
    print("thanks for playing.")
    break
else:
    input ("enter yes or no(y/n):")
    
  
  
    
    
    


