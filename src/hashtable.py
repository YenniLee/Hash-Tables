# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    def _repr_(self):
        return f"<{self.key}, {self.value}>"


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        # # store index of given key with _hash_mod()
        # index = self._hash_mod(key)
        
        # if self.storage[index] != None:
        #     print(f'ERROR: collision at index: [{index}]')
        # # insert into hash table
        # self.storage[index] = value

        #**********************Day 2****************
        index = self._hash_mod(key)
        # create linkedpair node using key/value
        new_node = LinkedPair(key, value)
        current_node = self.storage[index]
        # if no link at index
        if current_node == None:
            # set to new node
            self.storage[index] = new_node
        else:
            # set new node with key/value
           new_node.next = self.storage[index]
           # set index to new node
           self.storage[index] = new_node
                    
        

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        
        if self.storage[index] != None:
            self.storage[index] = None
        else:
            # print("ERROR: Key not found")
            return None



    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] == None:
            return None
        else:
            current_node = self.storage[index]
            while current_node:
                if current_node.key == key:
                    return current_node.value
                current_node = current_node.next



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage.copy()
        self.capacity = self.capacity * 2
        self.storage = [None] * self.capacity

        for item in old_storage:
            current = item
            while current:
                self.insert(current.key, current.value)
                current = current.next
              


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
    print(ht.storage)
