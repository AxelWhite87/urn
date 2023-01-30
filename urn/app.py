import re
from enum import Enum
from dataclasses import dataclass

class Category(Enum):
    FACT = 'fact'
    TASK = 'task'

def parse_line():
    """
    Parses the input and strips elements away one by one.  Once out of elements attempt to do that thing specified.
    """
    line = input().strip() # Get line input from user
    data: list[str] = line.split(" ") # Split the line based on spaces so we can get keywords out of it
    category: str = data.pop(0) # Since the first word is always the category we're affecting, snag it
    id: int = -1 # Hold the ID of a thing; -1 indicates no thing was passed
    modifiers: list[str] = [] # Hold any modifiers
    tags: list[str] = []
    action: str = "" # The action you want to do

    # Check if it's a valid category, if not kill the function
    if category not in [x.value for x in Category]:
        print("Invalid category!")
        return

    # If after removing the category the next item is an integer, remove it, cast it to int, and assign it to id
    if data[0].isdigit():
        id = int(data.pop(0))

    # At this point if the first term in the list is an action term and we have an ID, grab it and assign it
    if data[0] in ['modify', 'note', 'done', 'purge']:
        if id > -1: 
            action = data.pop(0)
        else:
            print("Action needs an ID, please try again.")
            return

    # Loop through all terms and remove and assign any modifiers and tags
    for term in data:
        if term.startswith("+") or term.startswith("-"):
            tags.append(term)
            data.remove(term)
        elif ":" in term:
            modifiers.append(term)
            data.remove(term)



if __name__ == "__main__":
    parse_line()
