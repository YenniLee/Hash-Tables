arr = []

arr =  [1, 2, 3, 4, 5]

# print(arr)
# print(id(arr))
# print(dir(arr))

"""['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']"""


"""
What is an array and how does it work?

- Stores a sequence of elements
- Each element must be the same data type
- Occupies a contiguous block of memory 
- Can access daa in constant time with this equation: memory_address = starting_address + index * data_size

*pointers -> memory_address*
"""

class DynamicArray: 
    def __init__(self, capacity=1):
        self.count = 0 # Number of elements in the array
        self.capacity = capacity # Total amount of storage in array
        self.storage = [None] * capacity
    
    def insert(self, index, value):
        # Check if there is enough capacity 
        if self.count >= self.capacity:
            # If not, add more capacity
            self.resize()
        # Shift over every item after index to the right by 1
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]
        # Add the new value to the index
        self.storage[index] = value
        # Increment count 
        self.count += 1
    
    def append(self, value):
        # Check if there is enough capacity 
        if self.count >= self.capacity:
            # If not, double the size 
            self.resize()
        # Add to the index of count (last index)
        self.storage[self.count] = value
        # Increment count
        self.count += 1
    
    def resize(self):
        # Double capacity
        self.capacity *= 2
        # Allocate a new storage array with double capacity
        new_storage = [None] * self.capacity
        # Copy all elements from old storage to new 
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage


a = DynamicArray(2)
a.insert(0, 10)
a.insert(0, 11)
print(a.storage)
a.append(9)
a.append(8)
print(a.storage)
a.append(7)

print(a.storage)


# O(n^2)
def add_to_front(n):
    x = []
    for i in range(0, n):
        x.insert(0, n - 1)
    return x

# O(n)
def add_to_back(n):
    x = []
    for i in range(0, n):
        x.append(i + 1)
    return x

# O(n)
def pre_allocate(n):
    x = [None] * n
    for i in range(0, n):
        x[i] = i + 1
    return x

import time

start_time = time.time()
add_to_back(10000) # O(n)
end_time = time.time()
print(f"runtime: {end_time - start_time} seconds")

start_time = time.time()
add_to_front(10000) # O(n^2)
end_time = time.time()
print(f"runtime: {end_time - start_time} seconds")



