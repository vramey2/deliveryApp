# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import Delivery
import Distances
import Package


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    Package.getPackageData()
Package.myHash.print()
#print (Distances.distanceList)
#print (Distances.addressList)
print (Distances.distances[16][1])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#print  (Distances.distanceBetween(' HUB',  ' 6351 South 900 East'))

#print(Distances.addresses [0])
print ('Distance is')
print (Distances.distanceBetween('195 W Oakland Ave', 'HUB'))


print ('truck')
#print("Truck: {}".format.Delivery.second_truck)

print ("Enter time in HH:MM:SS format: ")
input_time = input
(hour, minute, second) = input_time().split(":")
current_decimal_time = int(hour)*3600 + int(minute)*60 + int (second)
decimal_time = int(hour) + int(minute)/60 + int(second) / 3600
print ('current_decimal_time',  decimal_time)
input_package = int(input ("Enter package ID: "))
Delivery.lookupPackage(input_package, decimal_time)


print ('Enter time to look up all packages: ')
inputed_time = input
(hour, minute, second) = inputed_time().split(":")
current_d_time = int(hour)*3600 + int(minute)*60 + int (second)
d_time = int(hour) + int(minute)/60 + int(second) / 3600
#inputed_time = input
Delivery.getAll(d_time)


#user_selection = input ('Please chose the following options: \n'')