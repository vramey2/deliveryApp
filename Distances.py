import csv
import math

with open("Distances.csv") as distancedata:
    distances = list(csv.reader(distancedata, delimiter=','))
   # distanceList = list (distanceData)
   #  distances = []
   #  for row in distanceData:
   #     distances.append(row)

# print ('here are distances:')
# print (distances)


with open ("WGUPS Distance Table Rev.csv") as addressdata:
    addressdata = csv.reader(addressdata, delimiter= ',')
    addresses = list (addressdata)



def distanceBetween (address_one, address_two):
    indexone = addresses.index([address_one])
    indextwo = addresses.index([address_two])

    value = float (distances [indextwo] [indexone])

    return value

address_sequence = []


def minDistanceFrom (fromAddress, truck_addresses):

  distance = 0
#  address_sequence = []
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
     # print (distance)
      address_sequence.append([fromAddress, min_address, min_distance])
      truck_addresses.remove (fromAddress)


      minDistanceFrom(min_address, truck_addresses)


  return address_sequence



def routeTruck (address_sequence, truck_packages):
    truck_route = []
    for address1 in address_sequence:

        for i  in range (len(truck_packages)):

            if getattr(truck_packages[i], 'address') == address1[1]:
              truck_route.append(truck_packages[i])
    return truck_route


