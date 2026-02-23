import ast

project_list=[]
def menu():

    def add_task():
    
        while True: #asking the value again and again
            while True:
                try:
                    task_id=int(input("enter the task nid in number"))
                    break
                except ValueError:
                    print("please enter value in number ")
                    continue
            while True:
                task_name=input("Enter the name of the task ")
                if task_name.strip()=="":
                    print("Whitespaces and empty string Not allowed")
                    continue
                else:
                    break
            while True:
                task_status=input("enter the status: ")
                if not task_status:
                    task_status="pending"
                    break
                elif task_status.strip()=="":
                    print(" WHITESPACES ARE INVALID! ")
                    continue
                break
                
            
            dict={"Id":task_id,"Name":task_name,"Status":task_status}
            while True:
                try:
                    task_choice=int(input("do you want to add another task\n 1. Yes\n 2. No"))
                    if task_choice>2 or task_choice<1:
                        print("please enter valid number for option")
                        continue
                    else:
                        break
                except ValueError:
                    print("please enter the correct number")
                    continue
            
            if task_choice==1:
                project_list.append(dict)
                continue
            else:
                project_list.append(dict)
                break
        menu()
    
    
    def view_task():
        try:
            with open("project_file.txt","r") as file:
                print("Id\t Name\t Status")
                for line in file:
                    dict_line=ast.literal_eval(line)
                    print(f"{dict_line["Id"]}\t{dict_line["Name"]}\t{dict_line["Status"]}\n")
        except FileNotFoundError:
            print("File not found")
            menu()
    
    
    def save_task(project_list):
        try:
            with open("project_file.txt","a") as file:
                for i in project_list:
                    file.write(f"{str(i)}\n")
        except FileNotFoundError:
            with open("project_file.txt","w") as file:
                for i in project_list:
                    file.write(f"{str(i)}\n")
    
    while True:
        try:
            menu_choice=int(input("enter the option as a number: \n 1.Add Task\n 2.View Task \n 3.save and exit"))
            if menu_choice>3 or menu_choice<1:
                print("Enter the valid option number")
                continue
            else:
                break
        except ValueError:
            print("INVALID INPUT!,please enter the number for the option")
            continue

    if menu_choice==1:
        add_task()
    elif menu_choice==2:
        view_task()
    elif menu_choice==3:
        save_task(project_list)


menu()




