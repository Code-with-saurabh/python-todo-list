def user():
    Username=input("\nEnatr Your Username : ")
    Passowrd=input("\nEnatr Your Passowrd : ")
    user_detiels.append([Username,Passowrd])
    print(f"\n\nAccount Created Susccesfully...\n")
            
def login():
        Read_Username=input("\nEnter Your Username : ")
        Read_password=input("\nEnter Your password : ")
        i=0
        check(Read_Username,Read_password,i)
                     
def check(Read_Username,Read_password,i):
    if not user_detiels:
        print("\n\t\aNo Account exissit...")
        application()
        return
    else:
        for username,password in user_detiels:
            if username == Read_Username and password == Read_password:
                print(f"\n{Read_Username} Login Sucssecfully..\n")
                return
            elif username != Read_Username:
                i=i+1
                print("\n  Username Not Founde...")
                print("\n  Please Try again..")
                Read_Username=input("\nEnter Your Username : ")
                if i==4:
                    print("\n\tYou Try Multipule Time..\n")
                    print("\aExitiing The Program....")
                    application()
                    break
                else:
                    check(Read_Username,Read_password,i)
                
            elif password != Read_password:
                i=i+1
                print("\n Wrong Passowrd...")
                print("\n\tPlease Try again..")
                Read_password=input("\nEnter Your Passowrd : ")
                if i==4:
                    print("\n\tYou Try Multipule Time..\n")
                    print("\aExitiing The Program....")
                    application()
                    break
                else:
                    check(Read_Username,Read_password,i)
            else:
                print("\n"*20)
                print("\tWrong input...")              
            
def ToDoList():
    taskes=[]
    
    def taskeAdder():
        task=input("\nEnter A Task : ")
        taskes.append(task)
        print("\nTaske Added Susccesfully..")
        
    def viewtask():
        if not taskes:
            print("\nNo Take in list.")
            return
        else:
            print("\nTasks : ")
            j=0
            for i in taskes:
                    print(f"{j+1}.{i}")
                    j=j+1
                    
    def mark_tasks_Complete():
        viewtask()
        if not taskes:
            return
        else:
            task_index=int(input("\nEnter the task as complete : "))-1
            if 0<=task_index<len(taskes):
                print(f"\nTask '{taskes[task_index]}' matked as complete.")
                taskes.pop(task_index)
            else:
                print("\n\tinvalid task number.")
        
            
    while True:
        print("\n To-Do List Application \n")
        print("\n1. Add Task")
        print("\n2. View Task")
        print("\n3. Mark Task as Complete")
        print("\n4. Exit\n")
        choice=input("Enter Your Choice : ")
        
        if choice=="1":
            taskeAdder()
        elif choice=="2":
            viewtask()
        elif choice=="3":
            mark_tasks_Complete()
        elif choice=="4":
            print("Exitiing the Progarm..")
            break
        else:
            print("Invalid choice . please try again.")
 
print("\nWelcome To ToDoList Apllication\n")
def application():
    while True :
        print("\n1.Create An Account")
        print("\n2.login")
        print("\n3.Exit\n")
        choice=input("Entar Your Choice : ")
        if choice=="1":
            user()
        elif choice=="2":
            login()
            ToDoList()
        elif choice=="3":
            print("Exitiing The Program..")
            break
        else :
            print("\nWrong Choice Please Try Again...\n")
            
            
user_detiels=[]
application()  
