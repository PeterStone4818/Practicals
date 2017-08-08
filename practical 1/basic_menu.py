__author__ = 'Peter'

MENU = "(H)ello\n (G)oodbye\n (Q)uit"
name = input("What is your name?")
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
       print("Hello {}".format(name))
    elif choice == "G":
        print("Goodbye {}".format(name))
    else:
        print("Invalid Input")
    print(MENU)
