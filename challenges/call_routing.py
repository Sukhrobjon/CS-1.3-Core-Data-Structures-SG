# creating Trieclass

class TrieNode(object):
    def __init__(self, digit):
        
        self.digit = digit
        # initializing 10 children for each node because there are 10 digits possible
        self.children = [None] * 10
        # to indicate we traverse all the digits in the route
        self.end_path = False

        # consider having store the len of the route