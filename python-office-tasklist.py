office_tasklist = []            # first define a list

def add_task():                 # define add function, ask for user input and set a variable task  
    task = input("Please insert a task you want to add to your office-tasklist: \n")
    if task:
        office_tasklist.append(task)
        print(f"The task {task} was added to your list.")
    else:
        print("Your tasklist is empty.")

def show_tasklist():                        # define show tasklist function 
    if office_tasklist == None:             # check if tasklist is empty
        print("Your tasklist is empty.")
    else:
        for task in office_tasklist:        # enter a for -loop to print the input of the user
            print("Your tasklist:")        
            print(task)