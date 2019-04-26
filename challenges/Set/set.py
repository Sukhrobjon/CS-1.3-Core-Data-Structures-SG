#!python

from hashtable import HashTable

class Set(object):
    def __init__(self, elements=None):
        """Initialize set as an empty hash table."""
        self.table = HashTable()
        self.size = 0
        if elements:
            for elem in elements:
                self.table.set(elem, None)
                self.size += 1

    def __repr__(self):
        """Return a string representation of this Set."""
        items = ['{!r}'.format(key) for key in self.table.keys()]
        return '{' + ', '.join(items) + '}'

    def __iter__(self):
        """Return iterable set."""
        return iter(self.table.keys())

    def contains(self, elem):
        """Returns True if element is in the set and False otherwise."""
        # Pass the element as a key to call the hash table method contains().
        return self.table.contains(elem)

    def add(self, elem):
        """Add element to this set, if not present already"""
        if not self.contains(elem):  
            # Credit goes to Zurich Okoren for correcting me to pass correct params(None)
            self.table.set(elem, None)  
            self.size += 1
    

    def remove(self, elem):
        """Removes item to the set.
        Best and Worst case running time: O(1)"""
        if self.contains(elem):  
            self.table.delete(elem)
            self.size -= 1
        else:
            raise KeyError("Element: {} not in set.".format(elem))

    def union(self, other_set):
        """Return a new set that is the union of this set and other_set"""
        
        # copying the this set element to new_set
        new_set = Set(self.table.values()) 

        # now adds the other_set elements to the new set if not exist 
        for elem in other_set:    
            new_set.add(elem)  

        return new_set

    def difference(self, other_set):
        """Return a new set that is the difference of this set and other_set"""

        new_set = Set()

        for elem in self:
            if other_set.contains(elem) == False:
                # print("elem in difference: ", elem)
                new_set.add(elem)
        return new_set


    def intersection(self, other_set):
        """Return a new set that is the union of this set and other_set"""
        
        intersection_set = Set()
    
        small_set = self if self.size > other_set.size else other_set
        large_set = self if self.size < other_set.size else other_set
        
        # iterate through only small_set, so  
        for elem in small_set:
            if large_set.contains(elem): # found match from the large set
                intersection_set.add(elem)

        return intersection_set

    
        


    def symmetric_difference(self, other_set):
        """Return a new set that is the difference of both sets"""

        pass
    def is_subset(self, subset):
        """Return a boolean indicating whether other_set is a subset of this set"""

        pass


if __name__ == "__main__":
    s1 = Set([1, 2, 3, 5])
    print(s1)
    # s1 = s1.__iter__()
    # print(s1)
    for elem in s1:
        print(elem, end=", ")
    print()
   
    
    print("Size: ", s1.size)
    s2 = Set([2, 3, 4, 5, 8])
    print("Testing set functions!")
    s3 = s1.difference(s2)
    print("[1, 2, 3].differnce([2, 3, 4]):", s3)
    print("Intersection: ", s1, s2)
    print(s1.intersection(s2))
    
