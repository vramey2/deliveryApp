import csv

# Populates list of distances from given csv file
with open("Distances.csv") as distancedata:
    distances = list(csv.reader(distancedata, delimiter=','))

#Populates list of addresses from given csv file
with open ("WGUPS Distance Table Rev.csv") as addressdata:
    addressdata = csv.reader(addressdata, delimiter= ',')
    addresses = list (addressdata)


#Determines distance between two addresses
def distanceBetween (address_one, address_two):
    indexone = addresses.index([address_one])
    indextwo = addresses.index([address_two])

    value = float (distances [indextwo] [indexone])

    return value

address_sequence = []

# Algorithm uses nearest neighbour approach, it continues looking for the smallest distance to a given point
# Algorithm takes two paramenters: starting point and a list of all addresses
# Minimum distance is set at a high number
# The for loop compares distance between the starting address and the next address in the list, if minimum distance is
#Higher than the distance between to points, the miimum distance is assigned the value of that  poit and next address is appended to the
# sequence of the addresses in a route, appended address is removed from the list of all addresses.
# The function is recursive with a base case of the length of the list of addresses higher than 1. Returns sequence of addresses
# Complexity is O(n)
def minDistanceFrom (fromAddress, truck_addresses):

  distance = 0

  while len(truck_addresses) > 1:
      min_distance = 99999
      min_address = ' '

      for address2 in truck_addresses:
          if fromAddress == address2 :
              continue

          distance = distanceBetween(fromAddress, address2)


          if min_distance > distance:
              min_distance = distance
              min_address = address2

      distance += min_distance
      address_sequence.append([fromAddress, min_address, min_distance])
      truck_addresses.remove (fromAddress)


      minDistanceFrom(min_address, truck_addresses)


  return address_sequence


#Deterines route of a truck, parameters: sequence of addresses and a list of packages in a given truck
#Appends address to the truck's route if the address is in the list. Compexity O(n2)
def routeTruck (address_sequence, truck_packages):
    truck_route = []
    for address1 in address_sequence:

        for i  in range (len(truck_packages)):

            if getattr(truck_packages[i], 'address') == address1[1]:
              truck_route.append(truck_packages[i])
    return truck_route


