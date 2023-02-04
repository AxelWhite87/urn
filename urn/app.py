from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage
from tinydb.operations import decrement, set
from typing import Union

# db = TinyDb('urn.json')
db = TinyDB(storage=MemoryStorage)

query = Query()


def find_by_type(entry_type: str):
    if entry_type not in ['fact', 'task', 'track']:
        print("Invalid type supplied")
        return 
    return db.search(query.type == entry_type)

def delete_and_set_d_id(entry_type: str, id: int) -> None:
    d = query.d_id == id
    if not d:
        print(f"No {entry_type} of ID {id}")
        return
    db.remove(query.d_id == id)
    db.update(decrement('d_id'), query.d_id > id) 
    print(f"{entry_type} {id} deleted.")

def entry():
    db.insert({'type': 'fact', 'd_id': 1, 'text': 'I am a fact', 'notes': ['Note 1', 'Note 2']})
    db.insert({'type': 'task', 'd_id': 1, 'text': 'I am a second fact', 'isDone': False})
    db.insert({'type': 'fact', 'd_id': 2, 'text': 'Yep yep yep', 'tags': ['evil']})
    db.insert({'type': 'fact', 'd_id': 3, 'text': 'Yep yep yep', 'tags': ['evil']})
    db.insert({'type': 'fact', 'd_id': 4, 'text': 'Yep yep yep', 'tags': ['evil']})
    db.insert({'type': 'fact', 'd_id': 5, 'text': 'Yep yep yep', 'tags': ['evil']})
    db.insert({'type': 'task', 'd_id': 2, 'text': 'Yep yep yep', 'tags': ['evil'], 'isDone': True})
    db.insert({'type': 'task', 'd_id': 3, 'text': 'Yep yep yep', 'tags': ['evil'], 'isDone': False})

    # Get and print every entry with type of 'fact'
    # for result in db.search(query.type == 'fact'):
    #     print(result)

    # Same as above but in it's own function
    # print(find_by_type('task'))

    # Get an entry by it's ID and print it's first attached note
    # fact1 = db.get(doc_id=1)
    # print(fact1['notes'][0])

    # Find all entries that do not have the tag 'evil'
    # tag_test = db.search(~ query.tags.any(['evil']))
    # for t in tag_test:
    #     print(t)

    # Remove an entry and then decrement d_id of all subsequent entries
    # print(db.all())
    # db.remove(doc_ids=[3])
    # db.update(decrement('d_id'), query.d_id > 3)
    # print(db.all())

    # Remove an entry and update the d_ids in that type
    # for e in db.search(query.type == 'fact'):
    #     print(e)
    # print("===")
    # delete_and_set_d_id('fact', 3)
    # for e in db.search(query.type == 'fact'):
    #     print(e)

    print(db.search(query.type == 'task'))




if __name__ == "__main__":
    entry()


