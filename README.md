DNS Resolver Assignment
Overview

This Python script serves as a DNS resolver that leverages caching to efficiently resolve DNS queries. It processes queries from a specified DNS Queries file and checks against entries in a cache file. Queries resolved from the cache are printed immediately, while others are looked up in the DNS tree. Resolved queries are added to the cache; unresolved ones are marked as such.

DNS Tree Formatting

This DNS resolver navigates a simulated DNS hierarchy to resolve queries. The hierarchy is structured as follows:

    Root DNS Server: The top-level server in the DNS hierarchy (1-0-0-0.txt). It directs queries to the appropriate Top-Level Domain (TLD) server.
    TLD Server: Handles queries for domains within a specific top-level domain (.com, .edu, etc.).
    Authoritative Name Server: Provides the final IP address mapping for a specific domain.

Each server in the hierarchy is represented by a text file, named after the server's IP address, with entries formatted as domain;IP_address. For example, the root server might direct to a TLD server with com;15-25-72-200, indicating the .com TLD server is at IP 15.25.72.200. The resolver follows this format to dynamically navigate the DNS tree, resolving queries iteratively from the root to the authoritative server.

This approach simulates real DNS resolution within the constraints of this assignment, providing a practical understanding of DNS operations.

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

Author

    Israel Fernandez

Version

    1.0

Last Modified

    March 1, 2024