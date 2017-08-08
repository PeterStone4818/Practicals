def main():

    name = get_name()
    sliced_name = name[::2]
    print (sliced_name)


def get_name():
    name = input("please enter your name.")
    if len(name) < 1:
        print(input("Error, name cannot be blank."))
    return name


main()