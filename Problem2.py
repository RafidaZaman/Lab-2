#With any given number n,
# In any mobile, there is contact list. Create a list of contacts and then prompt the user to do the following:
# a) Display contact by name
# b) Display contact by number
# c) Edit contact by name
# d) Exit

def Mobile_contact():
    print('1. Display contact by name')
    print('2. Display contact by number')
    print('3. Edit contact by name')
    print('4. Quit')
    print()

numbers = {}
choice = 0
Mobile_contact()
while choice != 4:
    choice = int(input("Choose between 1 to 4: "))

    if choice == 1:   #Display Phonebook
        print("Phonebook:")
        for x in numbers.keys():
            print("Name: ", x, "\tNumber:", numbers[x])
        print()

    elif choice == 2:    #Display Numbers
        print("Display contact")
        name = input("Name: ")
        if name in numbers:
            print("contact number is", numbers[name])
        else:
            print(name, "not available")


    elif choice == 3:     #Edit Numbers
        print("Edit Name and Number")
        name = input("Name: ")
        # print("Remove Name and Number")
        # name = input("Name: ")
        if name in numbers:
           contact=numbers[name]
        contact = input("Number: ")
        numbers[name] = contact


    elif choice != 4:
        Mobile_contact()