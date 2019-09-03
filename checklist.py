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
    i = 0
    for item in checklist:
        print("{} {}".format(i,checklist))
        i += 1

def mark_completed(index):

    update(index, "V" + checklist[index])


def select(function_code):
    if function_code.lower() == "c":
        input_item = user_input("Input item: ")
        try: create(input_item)
        except:("Not a valid syntax")

    elif function_code.lower() == "r":
        item_index = user_input("Index Number? ")

        try: read(item_index)
        except: print("Not a valid index")

    elif function_code.lower() == "p":
        list_all_items()

    elif function_code.lower() == "q":
        return False

    elif function_code.lower() == "u":
        item_index = user_input("input index")
        updated_item = user_input("Input new item")
        try:
            update(item_index,updated_item)
        except:
            print ("Not a valid index")

    else:
        print("Unknown option")

    return True

def user_input(prompt):
    user_input = input(prompt)
    return user_input

running = True
while running:
    selection = user_input(
    "C to add to list \nR to read from list \nP to display list \nQ to quit \n")
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
