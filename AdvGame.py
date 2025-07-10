def intro():
    print("\n You are currently in a dark forest.")
    print("There is also a Anaconda in that forest who is defensing the treasure.\n")
    print("\n Your goal is to hunt the treasure with a safe movement and there are two directions(left / right).")
    direction= input("which side do you wanna go ? :").lower()
    if direction == "left":
        Anaconda_cave()
    elif direction == "right":
        treasure_hunt()
    else:
        print("invalid direction.")
        intro()
def Anaconda_cave():
    user_input=  input("You have two choices(run/ steal):").lower()
    if user_input == "run":
     print("you are safe and back to the jungle.")
     intro()
    elif user_input =="steal":
      print("you just got killed by Anaconda.")
      
    else:
      input("choose run or steal:")
      Anaconda_cave()
     
def treasure_hunt():
    print("you just found a room with gold and diamonds. ")
    user_choice=input("choose only one from them:").lower()
    if user_choice == "gold":
        print("you have successfully collected all the golds.")
        intro()
    elif user_choice== "diamonds":
        print("you have successfully collected all the diamonds.")
        intro()
    else:
        print("enter valid choice.")
        treasure_hunt()
intro()