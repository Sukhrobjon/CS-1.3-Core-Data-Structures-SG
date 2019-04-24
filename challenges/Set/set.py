#!python

from hashtable import HashTable

class Set(object):
    def __init__(self, elements=None):
        """Initialize set as an empty hash table."""
        self.table = HashTable()

        if len(elements) != 0:
            for elem in elements:
                self.table.set(elem, None)

    def __iter__(self):
        """Return iterable set."""
        return iter(self.table.keys())

    def __repr__(self):
        """Return a string representation of this Set."""
        items = ['{!r}'.format(key) for key in self.table.keys()]
        return '{' + ', '.join(items) + '}'

    def size(self):
        """Returns the number of elements in the set."""
    
        return self.table.length()  # O(1)

    def contains(self, elem):
        """Returns True if element is in the set and False otherwise.
        """

        # Pass the element as a key to call the hash table method contains().
        return self.table.contains(elem)

    def add(self, elem):
        """Add element to this set, if not present already"""
        if not self.contains(elem):  
            # Credit goes to Zurich Okoren for correcting me to pass correct params
            self.table.set(elem, None)  
        else:
            raise KeyError("Item is already in the set.")

    def remove(self, elem):
        """Removes item to the set.
        Best and Worst case running time: O(1)"""
        if self.contains(elem):  
            self.table.delete(elem)  
        else:
            raise KeyError("Element: {} not in set.".format(elem))

    def union(self, other_set):
        """Return a new set that is the union of this set and other_set"""
        
        new_set = Set()

        # first copies all elements from this set 
        for elem in self:  
           new_set.add(elem)  

        # now adds the other_set elements to the new set if not exist 
        for elem in other_set:  
            if new_set.contains(elem) != True:  
                new_set.add(elem)  

        return new_set

    def intersection(self, other_set):
        """Return a new set that is the union of this set and other_set"""

        pass

    def difference(self, other_set):
        """Return a new set that is the difference of this set and other_set"""

        pass

    def is_subset(self, subset):
        """Return a boolean indicating whether other_set is a subset of this set"""

        pass


if __name__ == "__main__":
    s1 = Set([1, 2, 3])
    print(s1)
    # for elem in s1:
    #     print(", ".join(elem))
