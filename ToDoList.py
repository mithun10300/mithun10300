print("Welcome to the task manager, what would you like to do.🙏🙏1")
tasks= [ ]

while (True):
    print("1. Show tasks")
    print("2. Remove task")
    print("3. Add tasks")
    print("4. Exit")
    
    choice = (input ("Choose a number(1-4):"))
    
    if choice == "1":
        if not tasks:
            print("No tasks available.")
        else:
            print("📚Your tasks :")
            for i, task in enumerate(tasks , 1):
                print(f"{i}. {tasks}")
                
                
    elif choice == "2":
        if not tasks:
            print("No tasks available❌.")
        else:
            for i, task in enumerate(tasks, 1):
              print(f"{i}. {tasks}")
              
            try:
                num= int(input("Enter task number to remove:"))
                if 1<= num <= len(tasks):
                   removed= tasks.pop(num-1)
                   print(f"🗑️Tasks removed :{removed}")
            except ValueError:
                print ("Enter a valid number.👎")
                
        
    elif choice == "3":
        task= input("📚Enter your task:")
        tasks.append(task)
        print("Task added.➕")
        
    elif choice == "4":
        print("Thank you for using.🙏")
        break
    else:
        print("Invalid choice.")

        

        
        
        