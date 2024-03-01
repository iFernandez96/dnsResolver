DNS Resolver Assignment
Overview

This Python script serves as a DNS resolver that leverages caching to efficiently resolve DNS queries. It processes queries from a specified DNS Queries file and checks against entries in a cache file. Queries resolved from the cache are printed immediately, while others are looked up in the DNS tree. Resolved queries are added to the cache; unresolved ones are marked as such.
Key Features

    Efficient DNS query resolution with caching.
    Reads and processes queries from files.
    Dynamically navigates the DNS tree for query resolution.
    Updates the cache with new resolutions.
    Identifies and marks unresolved queries.

Getting Started
Prerequisites

    Python 3.x

Installation

No installation required. The script can be executed directly in a Python 3 environment.
Usage

Execute the script from the command line by specifying the cache and DNS queries file paths:

bash
```bash
python3 main.py <cache-entries.txt> <dns-queries.txt>
```
File Descriptions

    main.py: The main Python script for DNS resolution.
    <cache-entries.txt>: Text file containing initial cache entries.
    <dns-queries.txt>: Text file with DNS queries to resolve.

How It Works

The script starts by reading the cache file and queries file. It then attempts to resolve each query, first checking the cache and, if not found, searching through the DNS tree. Successfully resolved queries are printed and added to the cache. The script ends by printing the final state of the cache.
Author

    Israel Fernandez

Version

    1.0

Last Modified

    March 1, 2024