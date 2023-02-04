from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage
from tinydb.operations import decrement
from typing import Union

# db = TinyDb('urn.json')
db = TinyDB(storage=MemoryStorage)

query = Query()


def find_by_type(entry_type: str):
    if entry_type not in ['fact', 'task', 'track']:
        print("Invalid type supplied")
        return 
    return db.search(query.type == entry_type)

def entry():
    db.insert({'type': 'fact', 'd_id': 1, 'text': 'I am a fact', 'notes': ['Note 1', 'Note 2']})
    db.insert({'type': 'task', 'd_id': 2, 'text': 'I am a second fact'})
    db.insert({'type': 'fact', 'd_id': 3, 'text': 'Yep yep yep', 'tags': ['evil']})
    db.insert({'type': 'fact', 'd_id': 4, 'text': 'Yep yep yep', 'tags': ['evil']})
    db.insert({'type': 'fact', 'd_id': 5, 'text': 'Yep yep yep', 'tags': ['evil']})
    db.insert({'type': 'fact', 'd_id': 6, 'text': 'Yep yep yep', 'tags': ['evil']})

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
    print(db.all())
    db.remove(doc_ids=[3])
    db.update(decrement('d_id'), query.d_id > 3)
    print(db.all())





if __name__ == "__main__":
    entry()


