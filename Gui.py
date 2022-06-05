import Delivery


def userGui(user_selection):
    if user_selection == '4':
        exit()
    # while user_selection != '3':
    if user_selection == '1':

        print("Enter time in HH:MM:SS format: ")
        input_time = input
        (hour, minute, second) = input_time().split(":")
        current_decimal_time = int(hour) * 3600 + int(minute) * 60 + int(second)
        decimal_time = int(hour) + int(minute) / 60 + int(second) / 3600
        print('current_decimal_time', decimal_time)
        input_package = int(input("Enter package ID: "))
        Delivery.lookupPackage(input_package, decimal_time)


    elif user_selection == '2':
        print('Enter time to look up all packages: ')
        inputed_time = input
        (hour, minute, second) = inputed_time().split(":")
        current_d_time = int(hour) * 3600 + int(minute) * 60 + int(second)
        d_time = int(hour) + int(minute) / 60 + int(second) / 3600

        Delivery.getAll(d_time)

    elif user_selection == '3':
        Delivery.total_distance()

    user_selection = input(print('Please chose the following options:  1 to look up package by ID and time\n ',
                        '2 to look up all packages at certain time \n', '3 to view total distance for 3 trucks\n',
                        '4 to exit'))

    userGui(user_selection)
