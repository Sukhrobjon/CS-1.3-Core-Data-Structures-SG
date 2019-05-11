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
    def __init__(self):
        self.root = TrieNode()
        self.size = 0
     
    def __repr__(self):
        "return A string represention of the Trie tree"
        return 'size: {}'.format(self.size)

    def add(self, route_number, price):
        """Add the new digit as node"""
        node = self.root
        
        # for index in range(1, len(route_number)):
        #     value = int(route_number[index])
        #     print("node: ",node)
        #     print(node.children)
        #     if node.children[value] == None:
        #         # assinging the children as new node
        #         node.children[value] == TrieNode()
        #         self.size += 1
        #     # updating the node
        #     node = node.children[value]
        # # attaching the price to last node 
        # node.price = price
        print("root: ", node)
        for index, digit in enumerate(route_number):
            # value = int(route_number[index])
            if node.children[int(digit)] == None:
                node.children[int(digit)] = TrieNode()
                node.digit = int(digit)
                self.size += 1
                print(node.digit)
                node.price = price
            if index == len(route_number)-1:
                break 
            node = node.children[int(digit)]

        print("last node: {}, node.digit: {} price: {}".format(node, node.digit, node.price))

if __name__ == "__main__":
    route = '1512'
    price = '0.04'

    obj = TrieTree()
    obj.add(route, price)
    print(obj)
    


