from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage
from tinydb.operations import set
from tabulate import tabulate

db = TinyDB(storage=MemoryStorage)
q = Query()


def set_display_ids(type: str) -> None:
    counter = 1
    for entry in db.search(q.type == type):
        print(entry.doc_id)
        db.update(set('display_id', counter), doc_ids=[entry.doc_id]) 
        counter += 1


def show_all():
    print(tabulate(db.all()))

def get(type: str, id: int):
    print(db.get(q.type == type and q.display_id == id))


def add_item(type: str, text: str) -> None:
    type = type.strip()
    text = text.strip()
    if type not in ['fact', 'task']:
        print(f"{type} is not a valid item type.")
        return
    new_item_id = db.insert({
        'type': type,
        'text': text
        })
    if type == "task":
        db.update(set('isDone', False), doc_ids=[new_item_id])
    set_display_ids(type)
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

        case 'fact':
          if not data[0]:

        case 'exit':
            print("Bye")
            break

        case other:
            print("Command not recognized.")
            continue
