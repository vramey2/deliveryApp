import Distances
import HashTable
import Package

first_truck = []
second_truck = []
third_truck = []


class Truck:

    def __init_self__(self, index, loaded_packages, start_time, maximum_capacity):
         self.index = index
         self.loaded_packages = []
         self.start_time = start_time
         self.maximum_capacity = maximum_capacity


first_start = 8.00
second_start = 9.10
third_start = 11.00

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

first_truck_addresses = []
for i  in range (len(first_truck)):
   first_truck_addresses.append(getattr(first_truck[i], 'address'))

# #first_truck_addresses.insert (0, 'HUB')
# print ("on first truck")
# print (first_truck_addresses)

first_addresses_noduplicates = list (set(first_truck_addresses))
first_addresses_noduplicates.insert(0, 'HUB')
# print ("first without dupblicates")
# print (first_addresses_noduplicates)

for package in second_truck:
    package.status = 'on truck 2'
    package.start_time = second_start
#print('on second truck')
second_truck_addresses = []
for i  in range (len(second_truck)):
    second_truck_addresses.append(getattr(second_truck[i], 'address'))



#print (second_truck_addresses)

second_addresses_noduplicates = list (set(second_truck_addresses))
second_addresses_noduplicates.insert (0, 'HUB')
# print ("second without dupblicates")
print (second_addresses_noduplicates)



for package in third_truck:
    package.status = 'on truck 3'
    package.start_time = third_start
#print ('third truck is ')
#print (third_truck)
third_truck_addresses = []
for i  in range (len(third_truck)):
   third_truck_addresses.append(getattr(third_truck[i], 'address'))

print ("on third truck")
#third_truck_addresses.insert(0, 'HUB')
third_addresses_noduplicates = list (set(third_truck_addresses))
third_addresses_noduplicates.insert (0, 'HUB')
#print (third_truck_addresses)

# print ('address sequence')
# print (Distances.minDistanceFrom( first_addresses_noduplicates[0], first_addresses_noduplicates))
first_addresse_sequence = Distances.minDistanceFrom(first_addresses_noduplicates [0], first_addresses_noduplicates)
#first_addresse_sequence.append('HUB')

#print ('first truck route')
first_sequence = Distances.minDistanceFrom(first_addresse_sequence[0], first_addresses_noduplicates)
first_route = Distances.routeTruck(first_sequence, first_truck)
# for package in first_route:
#     print (package)

first_index_list = []
for i in range (len(first_route)):
    first_index_list.append(first_route [i].id)
first_time = []
first_distance = []
j = 0
counter =  Distances.distanceBetween ('HUB', (getattr(first_route[0], 'address')))
for i in range (len(first_route)-1):
    distance = Distances.distanceBetween(first_route[i].address, first_route[i+1].address)
    counter += distance
    first_distance.append(counter)
   # delivery_time = first_start + counter/18
    first_time.append (first_start + counter/18)
   # package.delivery = delivery_time
for package in first_truck:
    package.status = 'on truck 1'
    package.start_time = first_start
    #index = getattr(package, 'id')
    #package.delivery = first_time [index]
first_distance.insert(0, Distances.distanceBetween ('HUB', (getattr(first_route[0], 'address'))))
first_distance.append(Distances.distanceBetween(getattr(first_route[-1], 'address'), 'HUB'))
first_time.append (first_start + (Distances.distanceBetween(getattr(first_route[-1], 'address'), 'HUB')/18))
for i in range (len(first_index_list)):
    index = first_index_list[i]
    Package.myHash.search(index).delivery = first_time[i]
   # package.delivery = first_time [first_index_list]
#print ('first times', first_time)
def getfirst_distance():
    return first_distance
#
# print ('first distances', first_distance)
# print ('first indexes', first_index_list)








#print  (vars(first_route))
#print (Distances.routeTruck(first_sequence, first_truck))
print ('first sequence', first_sequence)

second_addresses_sequence = Distances.minDistanceFrom(second_addresses_noduplicates[0], second_addresses_noduplicates)

print ('second truck route')
second_sequence = Distances.minDistanceFrom(second_addresses_sequence[0], second_addresses_noduplicates)
second_route = Distances.routeTruck(second_sequence, second_truck)
#second_route.append('HUB')
for package in second_route:
    print (package)

#second_addresses_sequence.append([getattr(second_route[-1], 'address'), 'HUB', Distances.distanceBetween(getattr(second_route[-1], 'address'), 'HUB')])
print ('second sequence')
print (second_addresses_sequence)
#print (second_addresses_sequence[1][2])
second_index_list = []
for i in range (len(second_route)):
    second_index_list.append(second_route [i].id)

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
#second distance


for i in range (len(second_index_list)):
    index = second_index_list[i]
    Package.myHash.search(index).delivery = second_time[i]



def getDistance(address_sequence):
    distance = 0.0
    for i in range (len(address_sequence)-1):
        if i == (len(address_sequence))-1:
            break
        value = address_sequence[i][2]
       # print ('value is')
        #print (value)
        #value_float = float (value)
        distance = distance + value

    return distance



# third truck route
print ('third sequence')
print (Distances.minDistanceFrom(third_addresses_noduplicates[0], third_addresses_noduplicates))
third_addresses_sequence = Distances.minDistanceFrom(third_addresses_noduplicates[0], third_addresses_noduplicates)
#third_addresses_sequence.append('HUB')


print ('third truck route')
third_sequence = Distances.minDistanceFrom(third_addresses_sequence[0], third_addresses_noduplicates)
third_route = Distances.routeTruck(third_sequence, third_truck)
for package in third_route:
    print (package)

#add returning to hub to the totals
# print ("distance total")
# last_one = Distances.distanceBetween(getattr(first_route[-1], 'address'), 'HUB') + Distances.distanceBetween(
#     getattr(second_route[-1], 'address'), 'HUB') + Distances.distanceBetween(getattr(third_route[-1], 'address'), 'HUB')
# distance =  getDistance(third_addresses_sequence) + last_one
# print (round (distance, 2))

def total_distance ():
    last_one = Distances.distanceBetween(getattr(first_route[-1], 'address'), 'HUB') + Distances.distanceBetween(
        getattr(second_route[-1], 'address'), 'HUB') + Distances.distanceBetween(getattr(third_route[-1], 'address'),
                                                                                 'HUB')
    distance = getDistance(third_addresses_sequence) + last_one

    print (round (distance, 2))
third_index_list = []
for i in range (len(third_route)):
    third_index_list.append(third_route [i].id)

third_time = []
third_distance = []
print ('third distances', third_distance)
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
print ('third distance times', third_time)
print ('first package indexes', first_index_list)

print ('first distances list', first_distance)
#def lookupAll (current_time):
for i in range (len(third_index_list)):
    index = third_index_list[i]
    Package.myHash.search(index).delivery = third_time[i]

def lookupPackage (packageID, current_time):
    if packageID in first_index_list:
        number = first_index_list.index(packageID)
        distance = first_distance[number]
        # for i in range (first_index_list.index(packageID)):
        #     distance += first_distance[i]
        #     print ("distance inside lookup", distance)
        time = distance/18
        start_time = 8.00
        #delta = current_time - start_time
        delivery_time = start_time + time
        formatted_delivery_hours = int(delivery_time)
        formatted_minutes = (time * 60) % 60
        formatted_seconds = (time * 3600 ) % 60
        formatted_string = "%d:%02d:%02d" % (formatted_delivery_hours, formatted_minutes, formatted_seconds)

        if current_time == start_time or current_time < start_time:
               print ('in the hub')
               first_route [number].status = 'in the hub'
               print(first_route[number])
        elif current_time > delivery_time:
            print ('status delivered')
            first_route[number].status = 'delivered at ',  formatted_string, distance
            print(first_route[number])
        elif current_time < delivery_time:
           print ('in route')
           first_route[number].status = 'in route'
           print(first_route[number])

        print ('time is ', time)
        #print ('number is', number)
    elif packageID in second_index_list:
            number = second_index_list.index(packageID)
            distance = second_distance[number]
            # for i in range(second_index_list.index(packageID)+1):
            #     distance += second_distance[i]
            time = distance / 18
            start_time = 9.10
            #delta = current_time + start_time
            delivery_time = start_time + time
            formatted_delivery_hours = int(delivery_time)
            formatted_minutes = (time * 60) % 60
            formatted_seconds = (time * 3600) % 60
            formatted_string = "%d:%02d:%02d" % (formatted_delivery_hours, formatted_minutes, formatted_seconds)

            if current_time == start_time or current_time < start_time:
                print('in the hub')
                second_route[number].status = 'in the hub'
                print (second_route [number])
            elif current_time > delivery_time:
                print('status delivered')
                second_route[number].status = 'delivered at ', formatted_string
                print(second_route[number])
            elif current_time < delivery_time:
                print('in route')
                second_route[number].status = 'in route'
                print(second_route[number])
            number = second_index_list.index(packageID)
            distance = second_distance [number]
            # distance = 0
            # for i in range(second_index_list.index(packageID)+1):
            #     distance += second_distance[i]
            time = distance / 18
            start_time = 9.10
            # delta = current_time + start_time
            delivery_time = start_time + time

            formatted_delivery_hours = int(delivery_time)
            formatted_minutes = (time * 60) % 60
            formatted_seconds = (time * 3600) % 60

            formatted_string = "%d:%02d:%02d" % (formatted_delivery_hours, formatted_minutes, formatted_seconds)

            if current_time == start_time or current_time < start_time:
                print('in the hub')
                second_route[number].status = 'in the hub'
                print(second_route[number])
            elif current_time > delivery_time:
                print('status delivered')
                second_route[number].status = 'delivered at ', formatted_string
                print(second_route[number])
                print('delivery time decimal')
                print(delivery_time)
            elif current_time < delivery_time:
                print('in route')
                second_route[number].status = 'in route'
                print(second_route[number])
    else:
            number = third_index_list.index(packageID)
            print ('number is ', number)
            distance = third_distance [number]
            # distance = 0
            # for i in range(third_index_list.index(packageID)+1):
            #         distance += third_distance[i]
            #         print ('index', i)
            time = distance / 18
            print ('and distance', distance)
            print ('calculated time', time)
            start_time = 11.00
            # delta = current_time + start_time
            delivery_time = start_time + time
            formatted_delivery_hours = int(delivery_time)
            formatted_minutes = (time * 60) % 60
            formatted_seconds = (time * 3600) % 60
            formatted_string = "%d:%02d:%02d" % (formatted_delivery_hours, formatted_minutes, formatted_seconds)

            if current_time == start_time or current_time < start_time:
                 #   print('in the hub')
                    print ('Package ID: ', third_route[number].id)
                    print ('Delivery address: ', third_route[number].address)
                    print ('Delivery deadline: ', third_route[number].deadline)
                    print ('Delivery city: ', third_route[number].city)
                    print ('Delivery zip code: ', third_route[number].zip)
                    print ('Package weight: ', third_route[number].weight)
                    print ('Delivery status: in the hub. To be delivered: ', formatted_string)
                   # third_route[number].status = 'in the hub'
                    #print(third_route[number])
            elif current_time > delivery_time:
                    print('status delivered')
                    third_route[number].status = 'delivered at ', formatted_string
                    print ('delivery time, decimal ', delivery_time)

                    print(third_route[number])
            elif current_time < delivery_time:
                    print('in route')
                    third_route[number].status = 'in route'
                    print (third_route[number])

            print('time is ', time)
            # print ('number is', number)

print ('third distances')
print (third_distance)
#lookupPackage(27, 12.03)

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




             #print('Package ID: ',  Package.get_myHash().get_item(str(i))[0] )
            # if start <= current_time:
                #  print ('in the hub')


        # print ('Package ID: ', getattr(package, 'id'))
        # if current_time <=  getattr(package, 'start_time'):
        #     print ('in the hub')
        # elif current_time > getattr(package, 'delivery'):
        #     print ('Delivered at', package.delivery)
        # else:
        #     print ('in the route')


#    for item in Package.myHash:
       # if package.start_time <= current_time:
          #  print ("Package ID: ", Package.myHash.id, ' in the hub')
       # Package.myHash.search()