"""
Module to get brewery information via the https://www.openbrewerydb.org/ API.
"""

import time
import asyncio
import requests as req
from pathlib import Path
from typing import List, Dict
import json
import socket

def get_brewery_count(state: str) -> Dict:
    """
    Retrieves information about breweries in a state and counts the number
    of breweries. Use page limit of 200 which is the max supported by the 
    Open Brewery DB API https://www.openbrewerydb.org/documentation.
    We use a combination of page and per_page arguments to get information
    about all the breweries in a state since a single API call only returns 
    a maximum of 200 breweries at a time. The page parameter is incremented by
    1 in every call until we get a non 200 response or an empty response.
 
    Args:
        state (string): The full name of a state, case insensitive.
 
    Returns:
        Dict: Dictionary with state name and brewery count. For example: {'state': 'maryland', 'count': 109}.
    """
    print(f"get_brewery_count, state={state}, entry")
    count = 0

    """
    YOUR CODE HERE.
    The OpenBrewery DB API URL is of the form "https://api.openbrewerydb.org/v1/breweries?by_state={state}&per_page=200&page={page}"
    keep incrementing the page number until the response json == [] or status_code != 200
    """
    
    print(f"get_brewery_count, state={state}, exiting")
    return dict(state=state, brewery_count=count)

async def async_get_brewery_count(state: str) -> Dict:
    """
    Wraps the get_brewery_count call into async.
    Args:
        state (string): The full name of a state, case insensitive.
 
    Returns:
        Dict: Dictionary with state name and brewery count
    """

    """
    YOUR CODE HERE
    """
    
async def get_brewery_counts_for_states(states: List[str]) -> List[Dict]:
    """
    Get count of breweries for a list of states in async manner.
    Args:
        state (List): The full name of a state, case insensitive.
 
    Returns:
         List[Dict]: List of dictionaries containing state name and brewery count
    """

    """
    YOUR CODE HERE
    """

if __name__ == "__main__":
    states = ['district_of_columbia', 'maryland', 'new_york', 'virginia']

    # async version
    s = time.perf_counter()
    brewery_counts = asyncio.run(get_brewery_counts_for_states(states))
    elapsed_async = time.perf_counter() - s
    print(f"{__file__}, brewery counts (async) -> {brewery_counts}, retrieved in {elapsed_async:0.2f} seconds")

    # serial version
    s = time.perf_counter()
    brewery_counts = [get_brewery_count(s) for s in states]
    elapsed_serial = time.perf_counter() - s
    print(f"{__file__}, brewery counts (serial) -> {brewery_counts}, retrieved in {elapsed_serial:0.2f} seconds")

    # async is faster..
    faster = 100*(elapsed_serial - elapsed_async) / elapsed_serial
    result_summary = f"async version was {faster:0.2f}% faster than the serial version"
    print(f"{__file__}, {result_summary}")

    # write result to a file
    Path("async.json").write_text(json.dumps({'result' : result_summary, 'host' : socket.gethostname()}))
