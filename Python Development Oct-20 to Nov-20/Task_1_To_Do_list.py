# Initialize an empty to-do list
to_do_list = []

# Function to add a task to the to-do list
def add_task(task):
    to_do_list.append(task)
    print("Task added: " + task)

# Function to update a task in the to-do list
def update_task(index, new_task):
    if (0 <= index < len(to_do_list)):
        to_do_list[index] = new_task
        print("Task updated at index : " + new_task)
    else:
        print("Invalid index.")

# Function to remove a task from the to-do list
def remove_task(index):
    if (0 <= index < len(to_do_list)):
        removed_task = to_do_list.pop(index)
        print("Task removed at index ", ": " + removed_task)
    else:
        print("Invalid index.")

# Function to display the current to-do list
def display_list():
    if (len(to_do_list)) == 0:
        print("To-Do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(to_do_list):
            print(str(index+1) + ": " + task)


print("--------------------------------------------------------")
print("|                   TO DO LIST                         |")
print("--------------------------------------------------------")
# Main loop to interact with the to-do list
while True:
    

    print("\nOptions:")
    print("1. Add a task")
    print("2. Update a task")
    print("3. Remove a task")
    print("4. Display the to-do list")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == "2":
        index = int(input("Enter the index of the task to update: "))
        new_task = input("Enter the new task: ")
        update_task(index, new_task)
    elif choice == "3":
        index = int(input("Enter the index of the task to remove: "))
        remove_task(index)
    elif choice == "4":
        display_list()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please select a valid option.")