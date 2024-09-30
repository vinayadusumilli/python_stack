from stack import Stack  # module


def get_preference(message) -> int:
    """
    Takes message to display and gets user input and return user input as int
    :param message: "Stack Memory\nLimit of Stack:
    :return:10
    """
    while True:
        try:
            return int(input(message))
        except ValueError as e:
            print(f"Not valid input, Reason: {e}")


create = True
while create:
    limit: int = get_preference(message="Stack Memory\nLimit of Stack: ")
    stack_ = Stack(limit)
    print(f"Stack created with size of {limit}")
    is_on = True
    while is_on:
        choice: int = get_preference(message="1. Add Element to Stack\n"
                                             "2. Remove Element from Stack\n"
                                             "3. Display Stack\n"
                                             "4. Initialize new Stack\n"
                                             "5. Quit\n"
                                             "Choose operation on your stack: ")
        if choice == 1:
            new_element: int = get_preference(message="Data to add in your stack: ")
            stack_.add_element(data=new_element)
        elif choice == 2:
            stack_.remove_element()
        elif choice == 3:
            stack_.display()
        elif choice == 4:
            confirm = get_preference(message=f"1. Confirm\n"
                                             f"2. Cancel\n"
                                             f"Are you sure you want to clear your stack and create a new one? ")
            if confirm == 1:
                is_on = False
        elif choice == 5:
            create = False
            break
        else:
            print("Invalid choose! Please try again.")
