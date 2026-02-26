''' 
The module provides following function:
ast: used for parsing string into corresponding python object
'''
import ast
project_list=[]
priority_list=["H","M","L"]
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
    while True:
        task_priority=input("Enter the task priority\n1.H\n2.M\n3.L").upper()
        if task_priority.upper() not in priority_list:
            print("enter the correct letter")
            continue
        break
    dictionary={"Id":task_id,"Name":task_name,"Status":task_status,"Priority":task_priority}
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

def view_task(project_list_p,menu_funct=None):
    '''
    This function displays the content of file in tabular format.
    '''
    print("Id \t Name       \t Status  \t Priority")
    for i in project_list_p:
        print(f"{i["Id"]} \t {i["Name"]} \t {i["Status"]}  \t{i["Priority"]}")
    if menu_funct is not None:
        menu_funct()

def save_task(project_list_p,menu_funct=None):
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
    if menu_funct is not None:
        menu_funct()
def mark_task_complete(menu_funct=None):
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
    if menu_funct is not None:
        menu_funct()
def sorted_task(menu_funct=None):
    '''
    This function sorts the tasks based on user input:

    The function sorts by:
    1.Status
    2.Priority
    3.Alphabet
    '''
    def sort_by_status():
        comparison_base={"pending":0,"completed":1}
        sorted_list=sorted(project_list,key=lambda x: comparison_base.get(x["Status"],99))
        view_task(sorted_list)
    def sort_by_priority():
        comparison_base={"H":0,"M":1,"L":2}
        sorted_list=sorted(project_list,key=lambda x: comparison_base.get(x["Priority"],99))
        view_task(sorted_list)
    def sort_by_alphabet():
        sorted_list=sorted(project_list,key=lambda x:x["Name"])
        view_task(sorted_list)
    while True:
        try:
            user_choice=int(input('''Enter the criteria for sorting
                1.Status
                2.Priority
                3.Alphabet'''))
        except ValueError:
            print("Enter the number correctly")
            continue
        if user_choice<1 or user_choice>3:
            print("Enter the number in range")
            continue
        break
    dict_choice={1:sort_by_status,2:sort_by_priority,3:sort_by_alphabet}
    dict_choice[user_choice]()
    if menu_funct is not None:
        menu_funct()
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
        menu()
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
                                  6.Search task
                                  7.sorted task'''))
            if menu_choice>7 or menu_choice<1:
                print("Enter the valid option number")
                continue
            break
        except ValueError:
            print("INVALID INPUT!,please enter the number for the option")
            continue
    dictionary_choice={1:add_task,2:lambda:view_task(project_list,menu),
                       3:lambda:save_task(project_list,menu),4:lambda:mark_task_complete(menu),
                       5:delete_task,6:search_task,
                       7:lambda:sorted_task(menu)}
    dictionary_choice[menu_choice]()
load_task()
