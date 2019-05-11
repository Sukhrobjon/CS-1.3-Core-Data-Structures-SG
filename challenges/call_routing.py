# creating Trieclass

class TrieNode(object):
    def __init__(self):
        """Initializing the node with list of 10 digits from 0-9 and store price"""
        self.digit = 0
        
        # initializing 10 children for each node because there are 10 digits possible
        self.children = [None] * 10
        #      
        self.price = 0
        
        
        # to indicate we traverse all the digits in the route
        self.end_path = False


        # consider having store the len of the route

    def __repr__(self):
        """Return a string representation of this trie node."""
        return 'TrieNode({!r})'.format(self.children)

class TrieTree(object):

    def __init__(self, routes=None):
        """Initialize trie tree with all routes"""
        self.root = TrieNode()
        self.size = 0
        if routes != None:
            for route, price in routes.items():
                self.add(route, price)
     
    def __repr__(self):
        "return A string represention of the Trie tree"
        return 'size: {}'.format(self.size)

    def add(self, route_number, price):
        """Add the new digit as node"""
        
        node = self.root
        print("root: ", node)
        for index, digit in enumerate(route_number):
            
            if node.children[int(digit)] == None:
                node.children[int(digit)] = TrieNode()
                node.digit = int(digit)
        
                self.size += 1
                # print(node.digit)
                node.price = price
            # if we hit the last digit in route we break out of loop don't update node 

            if index == len(route_number)-1:
                node.end_path = True
                break 
            # updating the node
            node = node.children[int(digit)] 
            

        # print("last node: {}, node.digit: {} price: {}".format(node, node.digit, node.price))
    def search(self, phone_number):
        """Return a price for givin phone number searching through Trie structured routes"""
        # start at the root
        node = self.root
        price = 0
        for digit in phone_number:
            # check if node exists where digit equals index
            if node.children[int(digit)] != None: 
                price = node.price
                node = node.children[int(digit)]
            else: # first unmatch digit and we break
                break 
        # return the price of last node
        return price
        
if __name__ == "__main__":
    route = '1415'
    price = '0.04'
    price_longer = '0.02'
    route_longer = '1415234'
    phone_number = '14152345678'
    obj = TrieTree()
    obj.add(route_longer, price_longer)
    # obj.add(route, price)
    
    print(obj)

    # Testing search

    print(obj.search(phone_number))


    


