checklist = list()

#CREATE
def create(item):
    checklist.append(item)
# READ
def read(index):
    item = checklist[int(index)]

#UPDATE
def update(index,item):
    checklist[index] = item

#DESTROY
def destroy(index):
    checklist.pop(index)

def printChecklist():
    i = 0
    for item in checklist:
        print("{} {}".format(i,checklist))
        i += 1


def mark_completed(index):

    update(index, "V" + checklist[index])


def select(function_code):
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    elif function_code == "R":
        item_index = user_input("Index Number?")

        read(item_index)

    elif function_code == "P":
        list_all_items()

    else:
        print("Unknown option")


def user_input(prompt):
    user_input = input(prompt)
    return user_input



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


running = True
while running:
    selection = user_input(
    "Press C to add to list, R to read from list and P to display list")
    select(selection)

index = 0

def list_all_items():
    for list_item in checklist:
      print(" {} {} ".format(index,list_item))
index += 1

list_all_items()
