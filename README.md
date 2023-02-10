# TODO

1. Get backend ORM all set for data.
2. Build out CLI to add, remove, and select data from database.
3. Build out CLI functions to show data.

# Architecture and Concept
The idea behind this is to capture notes during a live RPG sessions atomically as they happen in as natural a way possible.

Adding a note should be effortless.  So should retrieving one.  A simple syntax provides an interface to all your knowledge about a game.

Chronological notetaking can be accomplished by querying the timestamps on items.

Every item in the database is either a FACT or a TASK.

A FACT is a single conrete thing in the story.  For instance a character, a location, or a plot point.

A TASK is a goal to accomplish, either one of your character's or another in the setting.  Within the architecture, the only difference between a task and a fact is a task has a boolean on it that tells if it's done or not.

Each of these can have any number of NOTES, ATTRIBUTES, or LINKS

A NOTE is a single line that adds extra information to a fact or task.

An ATTRIBUTE is a key:value pair that describes something about the item.  It can be queried, for instance get strength of a character.

A LINK is a link between any item.  Such as two characters who know each other, a character involved in an ongoing plot point, etc.

# Command Structure

All commands are done as follows:

`category {id} action ...`

Where category is either Fact or Task, and ID is optionally supplied, and an action to do is provided.

Sample commands here:

fact add The hills are creepy //Adds fact
fact 1 // Retrieves fact 1
fact 1 modify +strahd // Adds tag 'strahd' to fact ID 1
fact hills // Retrieves any fact with 'hills' in the text
task add Kill strahd // Adds task
task 1 // Retrieves task 1
task 1 modify link:f1 // Links Fact ID 1 to task 1
fact 1 modify link:f2 // Links Fact ID 1 to Fact ID 2
task 1 done // Completes task 1
task 1 modify The hills aren't creepy after all // Updates the text of Fact ID 1
fact 1 note These hills ain't worth shit
task strahd // Retrieves any task with 'strahd' in the text

