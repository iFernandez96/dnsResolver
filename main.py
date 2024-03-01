import DNSNode
import DNSCache

# From https://docs.python.org/3/library/argparse.html
import argparse
# from https://www.geeksforgeeks.org/deque-in-python/
from collections import deque


def read_cache_file(filename):
    # Create the cache
    c = DNSCache.DNSCache()
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, ip = line.strip().split(";")
                c.add_node(DNSNode.DNSNode(name, ip))
    except FileNotFoundError:
        print("Cache file not found")
        exit()
    return c


def read_dns_file(filename):
    dns_queries = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                name = line.strip()
                dns_queries.append(name)
    except FileNotFoundError:
        print("DNS Queries file not found")
        exit()
    return dns_queries


def search_for_query(query, cache):
    query_in_parts = query.strip().split(".")
    query_in_parts_iterator = len(query_in_parts) - 1
    # Use a double ended queue to dynamically iterate through the DNS tree
    deque_to_iterare = deque(["1-0-0-0"])
    visited = []
    while deque_to_iterare:
        current = deque_to_iterare.pop()
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
                    cache.add_node(DNSNode.DNSNode(query, ip))
                    return True
                else:
                    if name == ".".join(query_in_parts[query_in_parts_iterator:]):
                        query_in_parts_iterator -= 1
                        deque_to_iterare.append(ip)
                        break
                    else:
                        continue
    print("Unresolved")
    return False


def main():
    # Setup the arguments
    args = argparse.ArgumentParser(description="DNS Resolver Assignment with Cache",
                                   usage='python3 %(prog)s [cache-entries.txt] [dns-queries.txt]')
    args.add_argument("cache")
    args.add_argument("dns")

    # Parse the arguments
    args = args.parse_args()

    # Read the cache file
    cache = read_cache_file(args.cache)

    # Print the cache
    # cache.print()

    # Read the DNS Queries file
    dns_queries = read_dns_file(args.dns)

    # Print the DNS Queries
    # print(dnsQueries)

    for query in dns_queries:
        print("Resolving Query: " + query.strip())
        if cache.get_node(query) is not None:
            print("Cache")
            print(query + ";" + cache.get_node(query).ip)
            continue
        else:
            search_for_query(query, cache)

    # Print the cache
    print("Current cache:")
    cache.print()


if __name__ == "__main__":
    main()
