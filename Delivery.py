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
#print  (vars(first_route))
#print (Distances.routeTruck(first_sequence, first_truck))

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

#second_addresses_sequence.append([getattr(second_route[-1], 'address'), 'HUB', Distances.distanceBetween(getattr(second_route[-1], 'address'), 'HUB')])
print ('second sequence')
print (second_addresses_sequence)
#print (second_addresses_sequence[1][2])


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