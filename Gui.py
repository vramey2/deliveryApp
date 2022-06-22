import Delivery
import Package

#Inteface for the uesr. Displays message and lets user make a selection.
def userGui():
    user_selection = input("""Please chose the following options:  1 to look up package by ID and time,
                                 2 to look up all packages at certain time,
                                 3 to view total distance for 3 trucks,
                                 4 to exit\n""")
    if user_selection == '4':
        exit()

    elif user_selection == '1':
        try:
            print("Enter time in HH:MM:SS format: ")
            input_time = input
            (hour, minute, second) = input_time().split(":")
            #current_decimal_time = int(hour) * 3600 + int(minute) * 60 + int(second)
            decimal_time = int(hour) + int(minute) / 60 + int(second) / 3600
            input_package = int(input("Enter package ID: "))
            lookUpFunction(input_package, decimal_time)
        except:
            print ('Please enter correct format for time and valid package number')


    elif user_selection == '2':
        try:
            print('Enter time to look up all packages: ')
            inputed_time = input
            (hour, minute, second) = inputed_time().split(":")
            d_time = int(hour) + int(minute) / 60 + int(second) / 3600
            getAll(d_time)
        except:
            print ('Please enter correct format for time')

    elif user_selection == '3':
        Delivery.total_distance()



    userGui()


# Look up delivery status by packageID and user entered time. Time complexity O(1).
# @param packageID and the time given by the user to look up status.
def lookUpFunction(packageID, current_time):
    myPackage = Package.myHash.get_item(packageID)
    start = myPackage.start_time
    delivery = myPackage.delivery

    formatted_delivery_hours = int(delivery)
    formatted_minutes = (delivery* 60) % 60
    formatted_seconds = (delivery * 3600) % 60
    formatted_string = "%d:%02d:%02d" % (formatted_delivery_hours, formatted_minutes, formatted_seconds)
    print('Package ID: ', myPackage.id)
    print('Delivery address: ', myPackage.address)
    print('Delivery deadline: ', myPackage.deadline)
    print('Delivery city: ', myPackage.city)
    print('Delivery zip code: ', myPackage.zip)
    print('Package weight: ', myPackage.weight)
    if start >=  current_time:

        print ('Delivery status: in the hub. To be delivered: ', formatted_string )

    elif current_time > delivery:

        print('Delivered at: ', formatted_string)
        # print('status delivered')

    elif current_time < delivery:
        print('In route. To be delivered at : ', formatted_string)


#Gets status of all packages at given time, O(n)
#Parameter is the time for which the status is looked up.
def getAll (current_time):

       for i in range(1, 41):
             start = Package.myHash.search(i).start_time
             delivery = Package.myHash.search(i).delivery
             formatted_delivery_hours = int(delivery)
             formatted_minutes = (delivery* 60) % 60
             formatted_seconds = (delivery * 3600) % 60
             formatted_string = "%d:%02d:%02d" % (formatted_delivery_hours, formatted_minutes, formatted_seconds)


             if start >= current_time:
                 print ('Package ID: ', i, ' in the hub')

             elif current_time >= delivery:
                 print ('Package ID: ', i, ' delivered at ', formatted_string)

             else:
                 print ('Package ID: ', i, ' in route, scheduled for delivery at ', formatted_string )

