# Description: A simple class that represents a DNS cache
# Author: Israel Fernandez

# Found from https://realpython.com/python-ordereddict/
from collections import OrderedDict

# Class that represents a DNS cache
class DNSCache:
    # Constructor
    def __init__(self):
        self.cache = OrderedDict()

    # Method to add a node to the cache
    def addNode(self, node):
        if len(self.cache) >= 3:
            self.deleteOldest()
        self.cache[node.name] = node

    # Method to remove a node from the cache
    def removeNode(self, name):
        del self.cache[name]

    # Method to get a node from the cache
    # if the node is found, move it to the most recent position
    def getNode(self, name):
        if name in self.cache:
            self.cache.move_to_end(name)
            return self.cache[name]
        return None

    # Method to delete the oldest node in the cache
    def deleteOldest(self):
          self.cache.popitem(last=False)

    # Method to print the cache
    def print(self):
        for node in self.cache.values():
            print(node.name, node.ip)