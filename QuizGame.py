def main():
   print("what is the national flower of Nepal ?")
   options= ["a. Rose ",
            "b. Lily",
            "c. Rhododendron",
            "d. Sunflower"
   ]
   print("\n here are your options:")
   for option in options:
    print(option)
    
   answer= input("choose a correct option:").lower()
  
   if answer== "c":
      print("congrats, you got a point.")
      
   elif answer in ['a' , 'b', 'd']:
      print("wrong answer!!")
      
   else:
      print("invalid option.")     
       
if __name__ == "__main__":
   main()
    
    
   