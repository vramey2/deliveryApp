
#class to create hash table using chaining to avoid collisions
class MyHashTable:

    #method to initialize the hash table using initial capacity. Capacity can be adjusted as needed
    def __init__(self, initial_capacity=40):

        self.table =[ [] for i in range (initial_capacity)]

    #  Method to insert new values into the hash table. If key is already in the bucket updates it and inserts new
    #value if key is not in the bucket into the end of the list.
    # O(n)
    def insert(self, key, item):
        for kv in self.table[hash(key) % len(self.table)]:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        self.table[hash(key) % len(self.table)].append([key, item])
        return True

    # To update existing value, complexity O(n)
    def update(self, key, item):
         if self.table [hash(key) % len(self.table)] != None:
                for kv in self.table [hash(key) % len(self.table)]:
                    if kv [0] == key:
                        kv[1] = item
                        return True

    # To find existing value, returns the value with complexity O(n)
    def get_item(self, key):
      #  bucket =  hash(key) % len(self.table)
        if self.table [hash(key) % len(self.table)] != None:
            for kv in self.table[hash(key) % len(self.table)]:
                if kv [0] == key:
                    return kv [1]



    # To search for value with existing key, returns either none if value not find or value 0(n)
    def search(self, key):
        for kv in self.table[hash(key) % len(self.table)]:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None

    # Method to delete item with the key that exists in the hash table, O(n)
    def remove(self, key):

        for kv in self.table[hash(key) % len(self.table)]:

            if kv[0] == key:
                self.table[hash(key) % len(self.table)].remove([kv[0], kv[1]])



2