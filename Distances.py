import csv
import math

with open("Distances.csv") as distancedata:
    distances = list(csv.reader(distancedata, delimiter=','))
   # distanceList = list (distanceData)
   #  distances = []
   #  for row in distanceData:
   #     distances.append(row)

print ('here are distances:')
print (distances)


with open ("WGUPS Distance Table Rev.csv") as addressdata:
    addressdata = csv.reader(addressdata, delimiter= ',')
    addresses = list (addressdata)



def distanceBetween (address_one, address_two):
    indexone = addresses.index([address_one])
    indextwo = addresses.index([address_two])

    value = float (distances [indextwo] [indexone])
    #if (value == None):
        #value = distances [indexone][indextwo]

   # print ('value')
    #print (value)

    return value

address_sequence = []
#distance = 0
def minDistanceFrom (fromAddress, truck_addresses):

  distance = 0
#  address_sequence = []
  while len(truck_addresses) > 1:
      min_distance = 99999
      min_address = ' '
     # distance = 0
     # address_sequence = []
      for address2 in truck_addresses:
          if fromAddress == address2 :
              continue

          distance = distanceBetween(fromAddress, address2)
          #print (distance)

          if min_distance > distance:
              min_distance = distance
              min_address = address2

      distance += min_distance
      print (distance)
      address_sequence.append([fromAddress, min_address, min_distance])
      truck_addresses.remove (fromAddress)


      minDistanceFrom(min_address, truck_addresses)

 # print ('total sequence distance')

 #total_distance = 0
  #for i in range (len(address_sequence)):
   #    total_distance +=  address_sequence[i[2]]
  print('distance inside')
  print(distance)
  return address_sequence



def routeTruck (address_sequence, truck_packages):
    truck_route = []
    for address1 in address_sequence:
       # if address_sequence.index(address1) == 0:
          #  continue
        for i  in range (len(truck_packages)):
           # index = truck_packages.index(address2)
            if getattr(truck_packages[i], 'address') == address1[1]:
              truck_route.append(truck_packages[i])
    return truck_route


