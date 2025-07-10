name= input("enter your name:")
print (f"Hello {name}, Welcome to this calculator.")
import math
Do_Again = True
used_time =0 
while(Do_Again):
  
  num1= int(input("num1:"))
  num2= int(input("num2:"))

  user_input= input("what do you want to do( +, - ,* , /):")
  
       
  if (user_input== "+"):
    
        print(f"sum:{num1 + num2}")
    
    
  elif (user_input== "*"):
    
        print(f"sum:{num1 * num2}")
    
  elif (user_input== "-"):
    
        print(f"sum:{num1 - num2}")
    
  elif (user_input== "/"):
    
        print(f"sum:{num1 / num2}")
    

  else:
    
        print("wrong input")
    
  again = input("reset, yes / no :").lower()
  if (again == "yes"):
    
        print( Do_Again)
  
    
  else:
    used_time += 1
    print(f"Thank you for using.you did {used_time} calculations.")
    
    break

    
    
    





