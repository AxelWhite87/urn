# TODO

1. Get backend ORM all set for data.
2. Build out CLI to add, remove, and select data from database.
3. Build out CLI functions to show data.

# Architecture
This uses Python's built in CLI + an ORM.

Originally the ORM was Pony, but after some research Peewee might be better suited.

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

