from uuid import UUID, uuid4
from pony.orm import *

# Stage our database in memory for testing
db = Database('sqlite', ':memory:')

# List out our model classes
class Fact(db.Entity):
    """Description of a discrete thing"""
    id = PrimaryKey(UUID, auto=True)
    simple_id = Required(int, unique=True)  # User facing ID
    text = Required(str)  # Text description
    game = Required('Game')  # The game the fact is linked to
    notes = Set('Note')  # Linked notes
    tags = Set('Tag')


class Game(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    name = Required(str, unique=True)
    facts = Set(Fact)
    tasks = Set('Task')


class Tag(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    text = Required(str, unique=True)
    facts = Set(Fact)
    tasks = Set('Task')


class Task(db.Entity):
    """Tasks to accomplish"""
    id = PrimaryKey(UUID, auto=True)
    simple_id = Required(int, unique=True)
    text = Required(str)
    done = Required(bool, default=False)
    game = Required(Game)
    notes = Set('Note')
    tags = Set(Tag)
    tracks = Set('Track')


class Note(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    text = Optional(str)
    fact = Optional(Fact)
    task = Optional(Task)


class Track(db.Entity):
    id = PrimaryKey(int, auto=True)
    task = Optional(Task)
    current_value = Required(int, sql_default='0')
    max_value = Required(int)
    text = Required(str)


# Generate tables, make them if they're missing
db.generate_mapping(create_tables=True)

## Class to hold all functions for interacting with the DB
@db_session
class DBContext:
    """Functions for interacting with the database"""

    def add_fact(self, text: str, game: Game):
        """
        Add a new Fact to the database.

        Attributes
        ----------
        text: str
            The text you want to add to the Fact
        game: Game
            The Game object the Fact is linked to
        """
        new_id = max(f.id for f in Fact) + 1 # Get the max value of Facts
        new_fact = Fact(simple_id=new_id, text=text, game=game)
        return new_fact.id


    def delete_fact(self, id: int) -> None:
        """
        Delete a fact from the database.

        Attributes
        ----------
        fact: Fact
            The fact object you are trying to delete
        """
        try:
            deleted_simple_id = Fact[id].simple_id
            Fact[id].delete()
            facts_to_update: Fact = select(f for f in Fact if f.simple_id > deleted_simple_id)
            for f in facts_to_update:
                f.simple_id -= 1 
            print(f"Deleted fact {id}")
        except Error as e:
            print(f"Unable to delete this fact ID {id}.  Reason: {e}")


    def modify_fact(self, id: int, modifiers: list[str]) -> None:
        """
        Modify a fact in the database

        Attributes
        ----------
        id: int
            The simple_id of the Fact to modify
        modifiers: list[str]
            A list of modifications to perform
        """
        # Get the Fact to update
        fact = Fact.get(simple_id=id)

        # Kill if it doesn't exist
        if fact == None:
            print(f"Unable to find Fact {id}")
            return

        for m in modifiers:
            if m.startswith("+") or m.startswith("-"):
                tag_modifier: str = m.pop(0)
                tag = self.find_or_create_tag(m)
                if tag_modifier == "+":
                    # Check if already has tag
                    pass
                else:
                    # Check if already doesn't have tag
                    pass


    def find_or_create_tag(self, text: str) -> Tag:
        """
        Find a tag based on it's text or create it

        Attributes
        ----------
        text: str
            The text of the string
        """
        tag = Tag.get(text=text)
        return tag if tag != None else Tag(text=text)