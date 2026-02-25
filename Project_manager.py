''' 
The module provides following function:
ast: used for parsing string into corresponding python object
'''
import ast
project_list=[]
def load_task():
    '''
    This function loads content of file into python list and calls another function.

    It opens file if exist and append each line of the file into a python list.
    If file does not exist, prints the message and calls another function.
    '''
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
    '''
    This functions adds tasks to the list.

    1. It takes the id,name and status of task as input from the user.
    2. Handels whitespaces, empty string and ValueError.
    3. Sets the default value for Status to pending.
    4. Stores the inputs into dictionary.
    5. Appends the dictionary to the list.
    '''
    while True:
        try:
            id_present=False
            task_id=int(input("enter the task nid in number"))

        except ValueError:
            print("please enter value in number ")
            continue
        for i in project_list:
            if i["Id"]==task_id:
                id_present=True
                break
        if id_present:
            print("Id already present")
            continue
        break
    while True:

        task_name=input("Enter the name of the task ")
        if task_name.strip()=="":
            print("Whitespaces and empty string Not allowed")
            continue
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
    dictionary={"Id":task_id,"Name":task_name,"Status":task_status}
    while True:
        try:
            task_choice=int(input("do you want to add another task\n 1. Yes\n 2. No"))
        except ValueError:
            print("please enter the correct number")
            continue
        if task_choice>2 or task_choice<1:
            print("please enter valid number for option")
            continue
        break
    if task_choice==1:
        project_list.append(dictionary)
        add_task()
    else:
        project_list.append(dictionary)
        menu()

def view_task():
    '''
    This function displays the content of file in tabular format.

    1. It opens the file, if not open prints the message and calls menu function.
    2. Parse each string into corresponding python object.
    3. Prints the those each object in tabular format.
    '''
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
    '''
    This function saves the user inputs into file
    
    1.Function takes 1 argument which is a list.
    2.Using loop, each index of list is converted into string and write in file
    3. Prints the message at last.
    4. Function neither return anything nor calls another function.
    '''
    with open("project_file.txt","w",encoding="utf-8") as file:
        for i in project_list_p:
            file.write(f"{str(i)}\n")
        print("Saved")

def mark_task_complete():
    '''
    This function marks the task as completed.

    1.Asks for the id 
    2.Checks if the id exist or not
    3.If exists, set status of that task as completed
    4.saves the task by calling save_task function
    '''
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
            if not id_in_list:
                print("id not in list")
                break
            save_task(project_list)
            break
        except ValueError:
            print("Please enter the number")
            continue

def menu():
    '''
    This function is menu driven.

    1. Prints the list of options
    2. calls the function according to the corrresponing number
    '''
    def delete_task():
        '''
        This function deletes the task based on user input.

        1. asks user for id
        2. Checks if id exist
        3. If exists delets the corresponding task
        4. If does not exist, prints the message and calls menu function
        '''
        while True:
            try:
                task_id=int(input("Enter the task id"))
            except ValueError:
                print("Please input the number of task id")
                continue
            task_id_present=False
            for i in project_list:
                if i["Id"]==task_id:
                    task_id_present=True
                    present_index=project_list.index(i)
                    break
            if task_id_present:
                user_confirmation=int(input("task found do you want to proceed\n1.Yes\n2.No"))
                if user_confirmation==1:
                    project_list.pop(present_index)
                    print("Task deleted")
                    save_task(project_list)
                    break
            else:
                print("Id is not present")
                menu()
                break
            break
    def search_task():
        '''
        This function search the task based on task name.

        1. Ask for user input.
        2.Search if name exist, case insensitive.
        3.If exist prints the corresponding task
        4.If does not exist, prints the message and calls menu function.

        '''
        task_name=input("enter the name of the task")
        task_name=task_name.lower()
        print("Id\tName\tStatus")
        title_match=False
        for i in project_list:
            if i["Name"].lower()==task_name:
                print(f"{i["Id"]}\t{i["Name"]}\t{i["Status"]}")
                title_match=True
                break
        if not title_match:
            print("No such title found")
            menu()
        menu()
    while True:
        try:
            menu_choice=int(input('''enter the option as a number:
                                  1.Add Task
                                  2.View Task
                                  3.save and exit
                                  4.mark task completed
                                  5.Delete task
                                  6.Search task'''))
            if menu_choice>6 or menu_choice<1:
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
    elif menu_choice==5:
        delete_task()
    elif menu_choice==6:
        search_task()
load_task()
