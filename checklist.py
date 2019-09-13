checklist = list()

#CREATE
def create(item):
    checklist.append(item)
# READ
def read(index):
    item = checklist[int(index)]
    print(item)

#UPDATE
def update(index,item):
    checklist[index] = item

#DESTROY
def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for item in checklist:
        print("{} {}\n".format(index,item))
        index += 1

def mark_completed(index):
    update(index, "√ " + checklist[index])


def select(function_code):
    try:

        if function_code.lower() == "c":
            input_item = user_input("Input item: ")
            create(input_item)
            return True

        elif function_code.lower() == "r":
            item_index = user_input("Index Number? ")
            read(item_index)
            return True

        elif function_code.lower() == "d":
            input_index = user_input("Index Number? ")
            destroy(int(input_index))
            return True

        elif function_code.lower() == "u":
            item_index = user_input("Index Number? ")
            input_item = user_input("Input item: ")
            update(int(item_index),str(input_item))
            return True

        elif function_code.lower() == "p":
            list_all_items()
            return True

        elif function_code.lower() == "q":
            return False

        elif function_code.lower() == "m":
            item_index = user_input("Index Number: ")
            mark_completed(int(item_index))
            return True

        else:
            print("Unknown option")
            return True

    except IndexError:
        print("This is not a valid input, please try again: ")
        return True

def user_input(prompt):
    user_input = input(prompt)
    return user_input

running = True
while running:
    selection = user_input(
    "C to add to list \nR to read from list \nP to display list \nQ to quit \nU to update an item\nD to destroy item\nM to mark complete\n")
    running = select(selection)


def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0,"purple socks")
    destroy(1)

    print(read(0))
    printChecklist()
    mark_completed(0)
    print(checklist[0])
    select("C")
    printChecklist()
    select("R")
    printChecklist()
    user_value = user_input("Please enter a value")
    print(user_value)


index = 0

list_all_items()
