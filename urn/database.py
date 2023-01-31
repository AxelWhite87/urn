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

set_sql_debug(True)
# Generate tables, make them if they're missing
db.generate_mapping(create_tables=True)

## Class to hold all functions for interacting with the DB
@db_session
class CliContext:
    """Functions for interacting with the database"""

    game_context: Game

    def add_game(self, name: str):
        """
        Create new game

        Attributes
        ----------
        text: str
            The name of the game
        """
        new_game = Game(name=name)
        print(f"Created new game '{new_game.name}'")

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
        new_id = max(f.id for f in Fact) + 1 if count(f for f in Fact) else 1# Get the max value of Facts
        new_fact = Fact(simple_id=new_id, text=text, game=game)
        print(f"Created new fact with ID {new_fact.simple_id}")


    def delete_fact(self, id: int) -> None:
        """
        Delete a fact from the database.

        Attributes
        ----------
        fact: Fact
            The fact object you are trying to delete
        """
        try:
            fact_to_delete: Fact = Fact.get(simple_id=id)
            deleted_simple_id = fact_to_delete.simple_id
            fact_to_delete.delete()
            facts_to_update: list[Fact] = select(f for f in Fact if f.simple_id > deleted_simple_id)
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
        fact: Fact = Fact.get(simple_id=id)

        # Kill if it doesn't exist
        if fact == None:
            print(f"Unable to find Fact {id}")
            return

        for m in modifiers:
            # Start with checking for tags
            if m.startswith("+") or m.startswith("-"):
                tag_modifier: str = m.pop(0)
                tag = self.find_or_create_tag(m)
                if tag_modifier == "+":
                    # Check if already has tag
                    if tag in fact.tags:
                        print(f"Fact {fact.simple_id} already has tag {tag.text}")
                    else:
                        fact.tags.add(tag)
                        print(f"Added {tag.text} to {fact.simple_id}")
                else:
                    # Check if already doesn't have tag
                    if tag not in fact.tags:
                        print(f"Fact {fact.id} already does not have tag {tag.text}")
                    else:
                        fact.tags.remove(tag)
                        print(f"Removed {tag.text} from {fact.simple_id}")
            # Next we check for links


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