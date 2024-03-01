import DNSNode
import DNSCache

# From https://docs.python.org/3/library/argparse.html
import argparse
# from https://www.geeksforgeeks.org/deque-in-python/
from collections import deque
def readCacheFile(filename):
    # Create the cache
    cache = DNSCache.DNSCache()
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, ip = line.strip().split(";")
                node = DNSNode.DNSNode(name, ip)
                cache.addNode(node)
    except FileNotFoundError:
        print("Cache file not found")
        exit()
    return cache


def readDNSFile(filename):
    dnsQueries = []
    try:
        with open(args.dns, 'r') as file:
            for line in file:
                name = line.strip()
                dnsQueries.append(name)
    except FileNotFoundError:
        print("DNS Queries file not found")
        exit()
    return dnsQueries

def searchForQuery(query, cache):
    queryInParts = query.strip().split(".")
    queryInPartsIterator = len(queryInParts) - 1
    # Use a double ended queue to dynamically iterate through the DNS tree
    dequeToIterare = deque(["1-0-0-0"])
    visited = []
    while dequeToIterare:
        current = dequeToIterare.pop()
        if current in visited:
            continue
        visited.append(current)
        with open(current + ".txt", 'r') as file:
            for line in file:
                name, ip = line.strip().split(";")
                if name == query:
                    visited.append(ip)
                    print(visited)
                    print(query + ";" + ".".join(ip.split("-")))
                    cache.addNode(DNSNode.DNSNode(query, ip))
                    return True
                else:
                    if name == ".".join(queryInParts[queryInPartsIterator:]):
                        queryInPartsIterator -= 1
                        dequeToIterare.append(ip)
                        break
                    else:
                        continue
    print("Unresolved")
    return False





if __name__ == '__main__':
    # Setup the arguments
    args = argparse.ArgumentParser(description="DNS Resolver Assignment with Cache",
                                   usage='python3 %(prog)s [cache-entries.txt] [dns-queries.txt]')
    args.add_argument("cache")
    args.add_argument("dns")

    # Parse the arguments
    args = args.parse_args()

    # Read the cache file
    cache = readCacheFile(args.cache)

    # Print the cache
    # cache.print()

    # Read the DNS Queries file
    dnsQueries = readDNSFile(args.dns)

    # Print the DNS Queries
    # print(dnsQueries)

    for query in dnsQueries:
        print("Resolving Query: ", query)
        if cache.getNode(query) is not None:
            print("Cache")
            print(query + ";" + cache.getNode(query).ip)
            continue
        else:
            searchForQuery(query, cache)

    # Print the cache
    print("Current cache:")
    cache.print()