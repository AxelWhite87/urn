# TODO

- [ ] Make configuration file and have it read in on launch
- [ ] Set ORM to handle all data storage and handling
- [ ] CLI commands to interact with the database and handle display
- [ ] Data export function

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

