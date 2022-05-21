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
def minDistanceFrom (fromAddress, truck_addresses):

 # address_sequence = []
  while len(truck_addresses) > 1:
      min_distance = 99999
      min_address = ' '
      distance = 0
      for address2 in truck_addresses:
          if fromAddress == address2 :
              continue

          distance = distanceBetween(fromAddress, address2)
          print (distance)

          if min_distance > distance:
              min_distance = distance
              min_address = address2

      address_sequence.append([fromAddress, min_address, min_distance])
      truck_addresses.remove (fromAddress)
      distance += min_distance
      minDistanceFrom(min_address, truck_addresses)

  print ('total sequence distance')

  total_distance = 0
  for i in address_sequence:
      total_distance += i[2]

  print (total_distance)
  return address_sequence

  # i = 0
  #  for i in range (len (truck_addresses)):
  #     for j in range ((i+1, (len(truck_addresses)-1)):
  #       value = distanceBetween(truck_addresses[i], truck_addresses[j]))
  #
  #
  #           if (value <= min):
  #                   min = value
  #                   truck_address_sequence.append (truck_addresses[j])
  #                   print ('appending address')
  #                   print (truck_addresses[j])
  #   return truck_address_sequence


    # for i in truck_addresses:
    #     value = i
    #     if distanceBetween(fromAddress, value) < min:
    #         min = distanceBetween(fromAddress, value)
    #         fromAddress = value
    #         truck_address_sequence.append(value)
    #         print ("appending address")
    #         print (value)
    # return truck_address_sequence