import Distances
import Package

# Create lists for the three trucks
first_truck = []
second_truck = []
third_truck = []


#  Assign time for the trucks to leave the hub
first_start = 8.00
second_start = 9.10
third_start = 11.00


#Load first truck
first_truck.append(Package.myHash.search(1))
first_truck.append(Package.myHash.search(4))
first_truck.append(Package.myHash.search(13))
first_truck.append(Package.myHash.search(14))
first_truck.append(Package.myHash.search(15))
first_truck.append(Package.myHash.search(16))
first_truck.append(Package.myHash.search(19))
first_truck.append(Package.myHash.search(20))
first_truck.append(Package.myHash.search(21))
first_truck.append(Package.myHash.search(34))
first_truck.append(Package.myHash.search(39))
first_truck.append(Package.myHash.search(40))

#Load second truck
second_truck.append(Package.myHash.search(3))
second_truck.append(Package.myHash.search(5))
second_truck.append(Package.myHash.search(6))
second_truck.append(Package.myHash.search(7))
second_truck.append(Package.myHash.search(8))
second_truck.append(Package.myHash.search(9))
second_truck.append(Package.myHash.search(18))
second_truck.append(Package.myHash.search(25))
second_truck.append(Package.myHash.search(26))
second_truck.append(Package.myHash.search(29))
second_truck.append(Package.myHash.search(30))
second_truck.append(Package.myHash.search(31))
second_truck.append(Package.myHash.search(32))
second_truck.append(Package.myHash.search(36))
second_truck.append(Package.myHash.search(37))
second_truck.append(Package.myHash.search(38))

#Load third truck
third_truck.append(Package.myHash.search(2))
third_truck.append(Package.myHash.search(10))
third_truck.append(Package.myHash.search(11))
third_truck.append(Package.myHash.search(12))
third_truck.append(Package.myHash.search(17))
third_truck.append(Package.myHash.search(22))
third_truck.append(Package.myHash.search(23))
third_truck.append(Package.myHash.search(24))
third_truck.append(Package.myHash.search(27))
third_truck.append(Package.myHash.search(33))
third_truck.append(Package.myHash.search(35))
third_truck.append(Package.myHash.search(28))

#Set statis pf 1st tricl [aclages as on truck 1
for package in first_truck:
    package.status = 'on truck 1'
    package.start_time = first_start


#Create and populate list with addresses of the first truck
first_truck_addresses = []
for i  in range (len(first_truck)):
   first_truck_addresses.append(getattr(first_truck[i], 'address'))


# Create list with addresses of the first truck without any duplicates
first_addresses_noduplicates = list (set(first_truck_addresses))
first_addresses_noduplicates.insert(0, 'HUB')

# Set status of 2nd truck packages as on truck 2
for package in second_truck:
    package.status = 'on truck 2'
    package.start_time = second_start


#Create and populate list with addresses of second truck
second_truck_addresses = []
for i  in range(len(second_truck)):
    second_truck_addresses.append(getattr(second_truck[i], 'address'))


#Create list with addresses of the second truck without any duplicates
second_addresses_noduplicates = list (set(second_truck_addresses))
second_addresses_noduplicates.insert (0, 'HUB')

#Set status of 3rd truck packages as on truck 3
for package in third_truck:
    package.status = 'on truck 3'
    package.start_time = third_start

#Create and populate list with addresses of third truck
third_truck_addresses = []
for i  in range (len(third_truck)):
   third_truck_addresses.append(getattr(third_truck[i], 'address'))

#Create list with addresses of the third truck without any duplicates
third_addresses_noduplicates = list (set(third_truck_addresses))
third_addresses_noduplicates.insert (0, 'HUB')

#Sequence of first truck addresses to route
first_addresse_sequence = Distances.minDistanceFrom(first_addresses_noduplicates [0], first_addresses_noduplicates)
first_sequence = Distances.minDistanceFrom(first_addresse_sequence[0], first_addresses_noduplicates)
first_route = Distances.routeTruck(first_sequence, first_truck)

#List of indices for the first truck
first_index_list = []
for i in range (len(first_route)):
    first_index_list.append(first_route [i].id)

#List of time and distance for the first truck
first_time = []
first_distance = []
j = 0
counter =  Distances.distanceBetween ('HUB', (getattr(first_route[0], 'address')))
for i in range (len(first_route)-1):
    distance = Distances.distanceBetween(first_route[i].address, first_route[i+1].address)
    counter += distance
    first_distance.append(counter)
    first_time.append (first_start + counter/18)

first_distance.insert(0, Distances.distanceBetween ('HUB', (getattr(first_route[0], 'address'))))
first_distance.append(Distances.distanceBetween(getattr(first_route[-1], 'address'), 'HUB'))
first_time.append (first_start + (Distances.distanceBetween(getattr(first_route[-1], 'address'), 'HUB')/18))

#insert delivery times to hash table for first truck
for i in range (len(first_index_list)):
    index = first_index_list[i]
    Package.myHash.search(index).delivery = first_time[i]



#Sequence of addresses for the second truck
second_addresses_sequence = Distances.minDistanceFrom(second_addresses_noduplicates[0], second_addresses_noduplicates)

#Second truck route. Second sequnce includes the first truck addresses
second_sequence = Distances.minDistanceFrom(second_addresses_sequence[0], second_addresses_noduplicates)

#List of addresses route for second truck
second_route = Distances.routeTruck(second_sequence, second_truck)

#List of indices for second truck
second_index_list = []
for i in range (len(second_route)):
    second_index_list.append(second_route [i].id)

#Time and distance for second truck
second_time = []
second_distance = []
counter = Distances.distanceBetween ('HUB', (getattr(second_route[0], 'address')))
j = 0
for i in range (len(second_route)-1):
    distance = Distances.distanceBetween(second_route[i].address, second_route[i+1].address)
    counter += distance
    second_distance.append(counter)
    second_time.append (second_start + counter/18)
second_distance.insert(0, Distances.distanceBetween ('HUB', (getattr(second_route[0], 'address'))))
second_distance.append(Distances.distanceBetween(getattr(second_route[-1], 'address'), 'HUB'))
second_time.append (second_start + (Distances.distanceBetween(getattr(second_route[-1], 'address'), 'HUB')/18))

for i in range (len(second_index_list)):
    index = second_index_list[i]
    Package.myHash.search(index).delivery = second_time[i]


# Get distance for a sequence of addresses
def getDistance(address_sequence):
    distance = 0.0
    for i in range (len(address_sequence)-1):
        if i == (len(address_sequence))-1:
            break
        value = address_sequence[i][2]
        distance = distance + value

    return distance



# Sequence of third truck addresses that appends to first and second sequence. and route for third truckto
third_addresses_sequence = Distances.minDistanceFrom(third_addresses_noduplicates[0], third_addresses_noduplicates)
third_sequence = Distances.minDistanceFrom(third_addresses_sequence[0], third_addresses_noduplicates)
third_route = Distances.routeTruck(third_sequence, third_truck)


#get total distance for all stops visited
def total_distance ():
    last_one = Distances.distanceBetween(getattr(first_route[-1], 'address'), 'HUB') + Distances.distanceBetween(
        getattr(second_route[-1], 'address'), 'HUB') + Distances.distanceBetween(getattr(third_route[-1], 'address'),
                                                                                 'HUB')
    distance = getDistance(third_addresses_sequence) + last_one

    print ('Total distance is: :', round (distance, 2))


#List of third truck package ids
third_index_list = []
for i in range (len(third_route)):
    third_index_list.append(third_route [i].id)

third_time = []
third_distance = []

j = 0
counter = Distances.distanceBetween ('HUB', (getattr(third_route[0], 'address')))
for i in range (len(third_route)-1):
    distance = Distances.distanceBetween(third_route[i].address, third_route[i+1].address)
    counter += distance
    third_distance.append(counter)
    third_time.append (third_start + counter/18)
   # Package.myHash.update(i,Package.package.delivery ) = (third_start + counter/18)
third_distance.insert(0, Distances.distanceBetween ('HUB', (getattr(third_route[0], 'address'))))
third_distance.append(Distances.distanceBetween(getattr(third_route[-1], 'address'), 'HUB'))
third_time.append (third_start + (Distances.distanceBetween(getattr(third_route[-1], 'address'), 'HUB')/18))
# print ('third distance times', third_time)
# print ('first package indexes', first_index_list)

# print ('first distances list', first_distance)
#def lookupAll (current_time):
for i in range (len(third_index_list)):
    index = third_index_list[i]
    Package.myHash.search(index).delivery = third_time[i]



#Look up delivery status by packageID and user entered time. Time complexity O(1)
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
def getAll (current_time):
   #for package in Package.get_myHash():
       for i in range(1, 41):
             start = Package.myHash.search(i).start_time
             delivery = Package.myHash.search(i).delivery
            # start = Package.get_myHash().get_item(str(i))[2]
             #print (start)
             #print (type(start))
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




