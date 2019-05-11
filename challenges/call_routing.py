# creating Trieclass

class TrieNode(object):
    def __init__(self):
        """Initializing the node with list of 10 digits from 0-9 and store price"""
        # self.digit = digit
        # initializing 10 children for each node because there are 10 digits possible
        self.children = [None] * 10
        #      
        self.price = 0
        
        
        # to indicate we traverse all the digits in the route
        self.end_path = False


        # consider having store the len of the route

class TrieTree(object):
    def __init__(self):
        self.root = TrieNode()
        self.size = 0
     
    def __repr__(self):
        "return A string represention of the Trie tree"
        return 'size: '.format(self.size)

    def add(self, route_number, price):
        """Add the new digit as node"""
        node = self.root
        for index in range(1, len(route_number)):
            value = int(route_number[index])
            if node.children[value] == None:
                # assinging the children as new node
                node.children[value] == TrieNode()
                self.size += 1
            # updating the node
            node = node.children[value]
        # attaching the price to last node 
        node.price = price
