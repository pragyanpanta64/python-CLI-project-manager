import ast 

project_list=[]
def load_task():
    try:
        with open("project_file.txt","r",encoding="utf-8") as file:
            content_list=file.readlines()
            for i in content_list:
                stripped_i=i.strip()
                dict_i=ast.literal_eval(stripped_i)
                project_list.append(dict_i)
            menu()

    except FileNotFoundError:
        print("File does the exist")
        menu()

def add_task():
    while True: #asking the value again and again
        #task ID
        while True:
            try:
                id_present=False
                task_id=int(input("enter the task nid in number"))
                for i in project_list:
                    if i["Id"]==task_id:
                        id_present=True
                        if id_present:
                            break
                if id_present:
                    print("Id already present")
                    continue
                break
                
            except ValueError:
                print("please enter value in number ")
                continue
        #task name
        while True:
            task_name=input("Enter the name of the task ")
            if task_name.strip()=="":
                print("Whitespaces and empty string Not allowed")
                continue
            else:
                break
        
        #task status
        while True:
            task_status=input("enter the status: ")
            if not task_status:
                task_status="pending"
                break
            elif task_status.strip()=="":
                print(" WHITESPACES ARE INVALID! ")
                continue
            break
            
        
        dictionary={"Id":task_id,"Name":task_name,"Status":task_status}
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
            project_list.append(dictionary)
            continue
        else:
            project_list.append(dictionary)
            break
    menu()
    

def view_task():
    try:
        with open("project_file.txt","r",encoding="utf-8") as file:
            print("Id\t Name\t Status")
            for line in file:
                dict_line=ast.literal_eval(line)
                print(f"{dict_line["Id"]}\t{dict_line["Name"]}\t{dict_line["Status"]}\n")
        menu()
    except FileNotFoundError:
        print("File not found")
        menu()

def save_task(project_list_p):
    
    with open("project_file.txt","w",encoding="utf-8") as file:
        for i in project_list_p:
            file.write(f"{str(i)}\n")
    
    

def mark_task_complete():
    while True:
        try:
            task_id=int(input("enter the id of the task"))
            id_in_list=False
            for i in project_list:
                if i["Id"]==task_id:
                    i["Status"]="completed"
                    print("Task completed")
                    id_in_list=True
                    break
            if id_in_list==False:
                print("id not in list")
                continue
            elif id_in_list:
                save_task(project_list)
                break
        except ValueError:
            print("Please enter the number")
            continue

def menu():
    while True:
        try:
            menu_choice=int(input('''enter the option as a number:
                                  1.Add Task
                                  2.View Task
                                  3.save and exit
                                  4.mark task completed'''))
            if menu_choice>4 or menu_choice<1:
                print("Enter the valid option number")
                continue
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
    elif menu_choice==4:
        mark_task_complete()
load_task()
