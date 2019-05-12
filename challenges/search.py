#!python


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    """Return the index of the targeted item"""
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    """Return the index of the targeted item"""
    if index >= len(array): # index is out of bound 
        return None  # not found
    elif array[index] == item:
        return index # found 
    else:
        return linear_search_recursive(array, item, index + 1) 



def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):

    left = 0
    right = len(array)-1
    
    while(left <= right):
        midpoint = (left + right) // 2
        print("midpoint: ", midpoint)
        
        if item == array[midpoint]:
            return midpoint

        elif item > array[midpoint]:
            left = midpoint + 1

        else:
            right = midpoint - 1
    
    return None # not found



def binary_search_recursive(array, item, left=None, right=None):
    
    if left == None and right == None:
        left = 0
        right = len(array) - 1
    midpoint = (left + right) // 2

    if item == array[midpoint]:
        return midpoint  # found
    
    if left > right:
        return None # not found

    elif item > array[midpoint]:
        left = midpoint + 1
        return binary_search_recursive(array, item, left, right)

    else:
        right = midpoint - 1
        return binary_search_recursive(array, item, left, right)
    
