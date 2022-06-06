import csv
import HashTable

first_truck = []
second_truck = []
third_truck = []

class Package:
    def __init__(self, id, address, deadline, city, state, zip, weight,  note, status, delivery, start_time):
        self.id = id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.state = state
        self.zip = zip
        self.weight = weight
        self.note = note
        self.status = status
        self.delivery = delivery
        self.start_time = start_time

    def __str__(self):  # overwite print(Movie) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.deadline, self.address, self.city, self.state, self.zip, self.weight, self.note, self.status, self.delivery, self.start_time)

def loadPackageData (filename, myHashTable):

    with open(filename) as packagedata:
        packageData = csv.reader(packagedata, delimiter= ',')
        next(packageData)
        
        for package in packageData:
            id = int (package[0])
            address = package [1]
            city = package [2]
            state = package [3]
            zip = package [4]
            deadline = package [5]
            weight = package [6]
            note = package [7]
            status = "In the hub"
            delivery = " "
            start_time = " "

         #   print ("inside for")

            if id == 9:
                address = '410 S State St'

                # package object
            newPackage = Package (id, address, deadline, city, state, zip, weight, note, status, delivery, start_time)
            #print ("New package" , newPackage)
            #insert into hash


            myHash.insert(id, newPackage)

def get_myHash():
    return myHash





myHash = HashTable.MyHashTable()
loadPackageData('packagedata.csv', myHash)

# #myHash.print()
# def getPackageData():
#      for i in range (len(myHash.table)+1):
#          print ("Package: {}".format(myHash.search(i+1)))
#
# getPackageData()