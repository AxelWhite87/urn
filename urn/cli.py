from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage
from tabulate import tabulate

db = TinyDB(storage=MemoryStorage)

def show_all():
    print(tabulate(db.all()))


def add_item(type: str, text: str):
    type = type.strip()
    text = text.strip()
    if type not in ['fact', 'task']:
        print(f"{type} is not a valid item type.")
        return
    new_item_id = db.insert({
        'type': type,
        'text': text
        })
    print(f"{type} {new_item_id} created.")


## Main CLI loop
while True:
    print("(CLI) ", end="")
    line = input().strip()
    data = line.split(" ")
    action = data.pop(0)
    match action:
        case 'show':
            show_all()
            continue
        case 'add':
            type = data.pop(0)
            add_item(type, " ".join(data))
            continue
        case 'exit':
            print("Bye")
            break
