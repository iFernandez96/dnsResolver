# Description: A simple class that represents a DNS node
# Author: Israel Fernandez
# Last Modified: 3/1/2024

# Class that represents a DNS node
class DNSNode:
    # Constructor
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip