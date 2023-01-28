import re
from enum import Enum

"""
Example commands:
fact The hills are creepy //Adds fact
fact 1 // Retrieves fact 1
fact 1 modify +strahd // Adds tag 'strahd' to fact ID 1
task Kill strahd // Adds task
task 1 // Retrieves task 1
task 1 modify link:f1 // Links Fact ID 1 to task 1
fact 1 modify link:f2 // Links Fact ID 1 to Fact ID 2
task 1 done // Completes task 1
task 1 modify The hills aren't creepy after all // Updates the text of Fact ID 1
fact 1 note These hills ain't worth shit
"""


def parse_line():
    line = input().strip()
    data = line.split(" ")
    category: str = data[0]
    if category == line:
        print(f"List all items from {category}")
        return

    if id := data[1].isdigit():
        print(f"Modifying {category} of id {id} with action {line}")
    else:
        print(f"Creating {category} of text '{line}'")

    return


if __name__ == "__main__":
    parse_line()
