#!/usr/bin/env python3
## This is the main file for the DNS Resolver Assignment
# The purpose of this assignment is to create a simple DNS resolver that uses a cache.
# The program will read a cache file and a DNS Queries file and resolve the queries.
# If a query is found in the cache, it will be printed. If not, the program will search for it in the DNS tree.
# If the query is found in the DNS tree, it will be printed and added to the cache.
# If the query is not found in the DNS tree, "Unresolved" will be printed.

# @Author: Israel Fernanadez
# @Last Modified: 3/1/2024
# @Version: 1.0

import DNSNode
import DNSCache

# From https://docs.python.org/3/library/argparse.html
import argparse
# from https://www.geeksforgeeks.org/deque-in-python/
from collections import deque


## This function will read the cache file and return a DNS cache
# @param filename: The name of the file to read
# @return: A DNS cache
# @throws FileNotFoundError: If the file is not found
def read_cache_file(filename):
    # Create the cache
    new_cache = DNSCache.DNSCache()
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, ip = line.strip().split(";")
                new_cache.add_node(DNSNode.DNSNode(name, ip))
    except FileNotFoundError:
        print("Cache file not found")
        exit()
    return new_cache


## This function will read the DNS Queries file and return a list of queries
# @param filename: The name of the file to read
# @return: A list of DNS queries
# @throws FileNotFoundError: If the file is not found
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


## This function will search for the query in the DNS tree
# @param query: The query to search for
# @param cache: The cache to use
# @return: True if the query was found, False otherwise
def search_for_query(query, cache):
    query_in_parts = query.strip().split(".")
    query_in_parts_iterator = len(query_in_parts) - 1
    # Use a double ended queue to dynamically iterate through the DNS tree starting from the root
    deque_to_iterare = deque(["1-0-0-0"])
    visited = []
    while deque_to_iterare:
        # Pop the current node from the deque
        current = deque_to_iterare.pop()

        # If the current node has been visited, skip it
        if current in visited:
            continue
        visited.append(current)

        # Open the file and search for the query
        try:
            with open(current + ".txt", 'r') as file:
                for line in file:
                    # Split the line into name and ip
                    name, ip = line.strip().split(";")
                    if name == query:
                        # We found the query!
                        visited.append(ip)
                        print(";".join(visited))
                        print(query + ";" + ".".join(ip.split("-")))
                        print()
                        cache.add_node(DNSNode.DNSNode(query, ip))
                        return True
                    else:
                        # Couldn't find the query, so we have to dig deeper into the tree
                        if name == ".".join(query_in_parts[query_in_parts_iterator:]):
                            query_in_parts_iterator -= 1
                            deque_to_iterare.append(ip)
                            break
                        else:
                            # Probably was not this line in the file, gotta check next one...
                            continue
        except FileNotFoundError:
            print("File not found")
    # Couldn't find the query at all starting from the root...
    print("Unresolved")
    print()
    return False


## This is the main function
def main():
    # Setup the arguments
    args = argparse.ArgumentParser(description="DNS Resolver Assignment with Cache",
                                   usage='python3 %(prog)s [dns-queries.txt] [cache-entires.txt]')
    args.add_argument("dns")
    args.add_argument("cache")

    # Parse the arguments
    args = args.parse_args()

    # Read the cache file
    cache = read_cache_file(args.cache)

    # Read the DNS Queries file
    dns_queries = read_dns_file(args.dns)

    # Process the DNS Queries
    for query in dns_queries:
        print("Resolving Query: " + query.strip())
        if cache.get_node(query) is not None:
            print("Cache")
            print(query + ";" + cache.get_node(query).ip)
            print()
            continue
        else:
            search_for_query(query, cache)

    print()
    # Print the cache
    print("Current cache:")
    cache.print()


if __name__ == "__main__":
    main()
