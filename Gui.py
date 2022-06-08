import Delivery


def userGui():
    user_selection = input("""Please chose the following options:  1 to look up package by ID and time,
                                 2 to look up all packages at certain time,
                                 3 to view total distance for 3 trucks,
                                 4 to exit\n""")
    if user_selection == '4':
        exit()
    # while user_selection != '3':
    elif user_selection == '1':
        try:
            print("Enter time in HH:MM:SS format: ")
            input_time = input
            (hour, minute, second) = input_time().split(":")
            #current_decimal_time = int(hour) * 3600 + int(minute) * 60 + int(second)
            decimal_time = int(hour) + int(minute) / 60 + int(second) / 3600
            input_package = int(input("Enter package ID: "))
            Delivery.getById(input_package, decimal_time)
        except:
            print ('Please enter correct format for time and valid package number')


    elif user_selection == '2':
        try:
            print('Enter time to look up all packages: ')
            inputed_time = input
            (hour, minute, second) = inputed_time().split(":")
            d_time = int(hour) + int(minute) / 60 + int(second) / 3600
            Delivery.getAll(d_time)
        except:
            print ('Please enter correct format for time')

    elif user_selection == '3':
        Delivery.total_distance()


   #user_selection = input
    userGui()
