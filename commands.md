# Manifest of commands
A full manifest of every possible command to implement

## Add a fact
```
fact add These hills are creepy
```

## Modify a fact
```
fact 1 modify These hills are less creepy
```

## Add note to a fact
```
fact 1 note Who owns them?
```

## Add a category to a fact
```
fact 1 modify cat:location
```

## Add a tag to a fact
```
fact 1 modify +evil
```

## Remove a tag from a fact
```
fact 1 modify -evil
```

## Add a new fact with a tag and a category
```
fact add Count Vladimir von Stradovich cat:character +evil
```

## Add a subcategory
```
fact 2 modify cat:evil.leader
```

## List all facts that match a tag
```
fact +evil
```

## List all facts that don't match a tag
```
fact -good
```

## Delete a fact
```
fact 2 purge
```
Prompts the user if they want to truly delete

# All above commands work for tasks and tracks

## Mark a task as done
```
task 1 done
```

## Mark all tasks that match a tag as done
```
task +evil done
```
Prompt with number of tasks to complete and Y/N

## Add new track
```
track add 3 Ki Points cat:sheet.resources
```

Tracks can be used to track resources and progress

## Delete a track
```
track 2 purge
```
