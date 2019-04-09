#!python


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
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
        return None
    elif array[index] == item:
        return index # found 
    else:
        return linear_search_recursive(array, item, index + 1) # not found



def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    left = 0
    right = len(array)-1
    print("right: ", right)
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
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

