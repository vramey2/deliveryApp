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



    #for value in range (1, len(Package.myHash))+1):
      # if Package.package ["note"] == 'on truck 2':
       #     second_truck.append()
#for i in range (len(Package.myHash.table)+1):
    #if Package.myHash [7] == "Can only be on truck 2":
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
for package in first_truck:
    package.status = 'on truck 1'

first_truck_addresses = []
for i  in range (len(first_truck)):
   first_truck_addresses.append(getattr(first_truck[i], 'address'))

#first_truck_addresses.insert (0, 'HUB')
print ("on first truck")
print (first_truck_addresses)

first_addresses_noduplicates = list (set(first_truck_addresses))
first_addresses_noduplicates.insert(0, 'HUB')
print ("first without dupblicates")
print (first_addresses_noduplicates)
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
for package in second_truck:
    package.status = 'on truck 2'
print('on second truck')
second_truck_addresses = []
for i  in range (len(second_truck)):
    second_truck_addresses.append(getattr(second_truck[i], 'address'))



   # print (getattr(second_truck[i], 'address'))

#second_truck_addresses.insert(0, 'HUB')
print (second_truck_addresses)
  #  print ('truck:')
second_addresses_noduplicates = list (set(second_truck_addresses))
second_addresses_noduplicates.insert (0, 'HUB')
print ("second without dupblicates")
print (second_addresses_noduplicates)

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
#third_truck_index = [2, 10, 11, 12, 17, 22, 23, 24, 27, 33, 35, 28]
for package in third_truck:
    package.status = 'on truck 3'
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

print ('address sequence')
print (Distances.minDistanceFrom( first_addresses_noduplicates[0], first_addresses_noduplicates))
first_addresse_sequence = Distances.minDistanceFrom(first_addresses_noduplicates [0], first_addresses_noduplicates)
#first_addresse_sequence.append('HUB')

print ('first truck route')
first_sequence = Distances.minDistanceFrom(first_addresse_sequence[0], first_addresses_noduplicates)
first_route = Distances.routeTruck(first_sequence, first_truck)
for package in first_route:
    print (package)

first_index_list = []
for i in range (len(first_route)):
    first_index_list.append(first_route [i].id)
first_time = []
first_distance = []
j = 0
for i in range (len(first_route)-1):
    distance = Distances.distanceBetween(first_route[i].address, first_route[i+1].address)
    first_distance.append(distance)
    first_time.append (distance/18)

first_distance.insert(0, Distances.distanceBetween ('HUB', (getattr(first_route[0], 'address'))))
first_distance.append(Distances.distanceBetween(getattr(first_route[-1], 'address'), 'HUB'))
first_time.append ((Distances.distanceBetween(getattr(first_route[-1], 'address'), 'HUB')/18))

print ('first times', first_time)
def getfirst_distance():
    return first_distance

print ('first distances', first_distance)
print ('first indexes', first_index_list)








#print  (vars(first_route))
#print (Distances.routeTruck(first_sequence, first_truck))
print ('first sequence', first_sequence)
# first_distances = []
# for i in range (len(first_route)-1):
#     first_distances.append(Distances.distances(getattr(Package.myHash.search(first_route[i], 'address')), getattr(Package.myHash.search(first_route[i+1], 'address'))))
# first_distances.append(Distances.distanceBetween(first_sequence[-1] [1], 'HUB'))
# print ('first distances list')
# print (first_distances)
# second truck route
#print ('second sequence')
#print (Distances.minDistanceFrom(second_addresses_noduplicates[0], second_addresses_noduplicates))
second_addresses_sequence = Distances.minDistanceFrom(second_addresses_noduplicates[0], second_addresses_noduplicates)

print ('second truck route')
second_sequence = Distances.minDistanceFrom(second_addresses_sequence[0], second_addresses_noduplicates)
second_route = Distances.routeTruck(second_sequence, second_truck)
#second_route.append('HUB')
for package in second_route:
    print (package)

# irst_index_list = []
# for i in range (len(first_route)):
#     first_index_list.append(first_route [i].id)
# first_time = []
# first_distance = []
# j = 0
# for i in range (len(first_route)-1):
#     distance = Distances.distanceBetween(first_route[i].address, first_route[i+1].address)
#     first_distance.append(distance)
#     first_time.append (distance/18)
#
# first_distance.append(Distances.distanceBetween(getattr(first_route[-1], 'address'), 'HUB'))
# first_time.append ((Distances.distanceBetween(getattr(first_route[-1], 'address'), 'HUB')/18))

#second_addresses_sequence.append([getattr(second_route[-1], 'address'), 'HUB', Distances.distanceBetween(getattr(second_route[-1], 'address'), 'HUB')])
print ('second sequence')
print (second_addresses_sequence)
#print (second_addresses_sequence[1][2])
second_index_list = []
for i in range (len(second_route)):
    second_index_list.append(second_route [i].id)

second_time = []
second_distance = []
j = 0
for i in range (len(second_route)-1):
    distance = Distances.distanceBetween(second_route[i].address, second_route[i+1].address)
    second_distance.append(distance)
    second_time.append (distance/18)
second_distance.insert(0, Distances.distanceBetween ('HUB', (getattr(second_route[0], 'address'))))
second_distance.append(Distances.distanceBetween(getattr(second_route[-1], 'address'), 'HUB'))
second_time.append ((Distances.distanceBetween(getattr(second_route[-1], 'address'), 'HUB')/18))
#second distance
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
print ("distance total")
last_one = Distances.distanceBetween(getattr(first_route[-1], 'address'), 'HUB') + Distances.distanceBetween(
    getattr(second_route[-1], 'address'), 'HUB') + Distances.distanceBetween(getattr(third_route[-1], 'address'), 'HUB')
distance =  getDistance(third_addresses_sequence) + last_one
print (round (distance, 2))

third_index_list = []
for i in range (len(third_route)):
    third_index_list.append(third_route [i].id)

third_time = []
third_distance = []
j = 0
for i in range (len(third_route)-1):
    distance = Distances.distanceBetween(third_route[i].address, third_route[i+1].address)
    third_distance.append(distance)
    third_time.append (distance/18)
third_distance.insert(0, Distances.distanceBetween ('HUB', (getattr(third_route[0], 'address'))))
third_distance.append(Distances.distanceBetween(getattr(third_route[-1], 'address'), 'HUB'))
third_time.append ((Distances.distanceBetween(getattr(third_route[-1], 'address'), 'HUB')/18))

print ('first package indexes', first_index_list)

print ('first distances list', first_distance)
def lookupPackage (packageID, current_time):
    if packageID in first_index_list:
        number = first_index_list.index(packageID)
        distance = 0
        for i in range (first_index_list.index(packageID)):
            distance += first_distance[i]
            print ("distance inside lookup", distance)
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
            distance = 0
            for i in range(second_index_list.index(packageID)):
                distance += second_distance[i]
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
            distance = 0
            for i in range(second_index_list.index(packageID)):
                distance += second_distance[i]
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
            elif current_time < delivery_time:
                print('in route')
                second_route[number].status = 'in route'
                print(second_route[number])
    else:
            number = third_index_list.index(packageID)
            distance = 0
            for i in range(third_index_list.index(packageID)):
                    distance += third_distance[i]
            time = distance / 18
            start_time = 11.00
            # delta = current_time + start_time
            delivery_time = start_time + time
            formatted_delivery_hours = int(delivery_time)
            formatted_minutes = (time * 60) % 60
            formatted_seconds = (time * 3600) % 60
            formatted_string = "%d:%02d:%02d" % (formatted_delivery_hours, formatted_minutes, formatted_seconds)

            if current_time == start_time or current_time < start_time:
                    print('in the hub')
                    third_route[number].status = 'in the hub'
                    print(third_route[number])
            elif current_time > delivery_time:
                    print('status delivered')
                    third_route[number].status = 'delivered at ', formatted_string
                    print(third_route[number])
            elif current_time < delivery_time:
                    print('in route')
                    third_route[number].status = 'in route'
                    print (third_route[number])

            print('time is ', time)
            # print ('number is', number)


#lookupPackage(27, 12.03)
