import csv
import HashTable


class Package:
    def __init__(self, id, address, deadline, city, state, zip, weight, status):
        self.id = id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.state = state
        self.zip = zip
        self.weight = weight
        self.status = status

    def __str__(self):  # overwite print(Movie) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.deadline, self.address, self.city, self.state, self.zip, self.weight, self.status)

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
            status = "In the hub"

         #   print ("inside for")



                # package object
            newPackage = Package (id, address, deadline, city, state, zip, weight, status)
            print ("New package" , newPackage)
            #insert into hash
            myHash.insert(id, newPackage)
myHash = HashTable.MyHashTable()
loadPackageData('packagedata.csv', myHash)
myHash.print()
def getPackageData():
     for i in range (len(myHash.table)+1):
         print ("Package: {}".format(myHash.search(i+1)))

getPackageData()