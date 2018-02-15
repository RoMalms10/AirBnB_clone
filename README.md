# Airbnb Clone - The Command Interpreter
![Image of Holberton B&B Logo](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png)
## Airbnb Clone - Command Interpreter Project Description
### This is a multi-part project which will result in a complete clone of the Airbnb website, both front-end and back-end. For this part of the project using Python programming language, we will build a command interpreter for the cloned web app. A command interpreter is very similar to the BASH shell, but designed for a specific use case.
## How to start the interpreter
### From the command line run ./console.py or echo "help" | ./console.py
## Usage
### Included with the basic interpreter are console commands EOF, quit, help, create, destroy, update, show, and all.

Command | Syntax | Output
------- | ------ | ------
help | help *[option]* | list of all available commands, or displays what option does
quit | quit | exit command interpreter
EOF | EOF | exit command interpreter
create | create *[class_name]* | creates an instance of class_name
update | update *[class_name] [object_id] [update_key] [update_value]* | updates the key:value of class_name.object_id instance
show | show *[class_name] [object_id]* | displays all attributes of class_name.object_id
all | all *[class_name]* | displays every instance of class_name, without option displays every instance saved to file
destroy | destroy *[class_name] [object_id]* | deletes all attributes of class_name.object_id

## Examples
```python3
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) all
[]
(hbnb) create User
1083ad5b-d1f5-4273-a13e-f83651c24cca
(hbnb) show User 1083ad5b-d1f5-4273-a13e-f83651c24cca
[User] (1083ad5b-d1f5-4273-a13e-f83651c24cca) {'created_at':
datetime.datetime(2018, 2, 15, 23, 31, 2, 164460), 'id':
'1083ad5b-d1f5-4273-a13e-f83651c24cca', 'updated_at':
datetime.datetime(2018, 2, 15, 23, 31, 2, 164468)}
(hbnb) update User 1083ad5b-d1f5-4273-a13e-f83651c24cca 'name' 'Shannon'
(hbnb) show User 1083ad5b-d1f5-4273-a13e-f83651c24cca
[User] (1083ad5b-d1f5-4273-a13e-f83651c24cca) {'name': 'Shannon', 'created_at':
datetime.datetime(2018, 2, 15, 23, 31, 2, 164460), 'updated_at':
datetime.datetime(2018, 2, 15, 23, 31, 2, 164468), 'id':
'1083ad5b-d1f5-4273-a13e-f83651c24cca'}
(hbnb) create Place
a2e97dbb-b4ea-4014-b4a2-82b3b72aa52d
(hbnb) show Place a2e97dbb-b4ea-4014-b4a2-82b3b72aa52d
[Place] (a2e97dbb-b4ea-4014-b4a2-82b3b72aa52d) {'created_at':
datetime.datetime(2018, 2, 15, 23, 32, 14, 428503), 'id':
'a2e97dbb-b4ea-4014-b4a2-82b3b72aa52d', 'updated_at':
datetime.datetime(2018, 2, 15, 23, 32, 14, 428507)}
(hbnb) all
[[Place] (a2e97dbb-b4ea-4014-b4a2-82b3b72aa52d) {'created_at':
datetime.datetime(2018, 2, 15, 23, 32, 14, 428503), 'id':
'a2e97dbb-b4ea-4014-b4a2-82b3b72aa52d', 'updated_at':
datetime.datetime(2018, 2, 15, 23, 32, 14, 428507)}, [User]
(1083ad5b-d1f5-4273-a13e-f83651c24cca) {'name': 'Shannon', 'created_at':
datetime.datetime(2018, 2, 15, 23, 31, 2, 164460), 'updated_at':
datetime.datetime(2018, 2, 15, 23, 31, 2, 164468), 'id':
'1083ad5b-d1f5-4273-a13e-f83651c24cca'}]
(hbnb) all User
[[User] (1083ad5b-d1f5-4273-a13e-f83651c24cca) {'name': 'Shannon',
'created_at': datetime.datetime(2018, 2, 15, 23, 31, 2, 164460), 'updated_at':
datetime.datetime(2018, 2, 15, 23, 31, 2, 164468), 'id':
'1083ad5b-d1f5-4273-a13e-f83651c24cca'}]
(hbnb) all Place
[[Place] (a2e97dbb-b4ea-4014-b4a2-82b3b72aa52d) {'created_at':
datetime.datetime(2018, 2, 15, 23, 32, 14, 428503), 'id':
'a2e97dbb-b4ea-4014-b4a2-82b3b72aa52d', 'updated_at':
datetime.datetime(2018, 2, 15, 23, 32, 14, 428507)}]
(hbnb) destroy Place a2e97dbb-b4ea-4014-b4a2-82b3b72aa52d
(hbnb) all
[[User] (1083ad5b-d1f5-4273-a13e-f83651c24cca) {'name': 'Shannon', 'created_at':
datetime.datetime(2018, 2, 15, 23, 31, 2, 164460), 'updated_at':
datetime.datetime(2018, 2, 15, 23, 31, 2, 164468), 'id':
'1083ad5b-d1f5-4273-a13e-f83651c24cca'}]
(hbnb)
```
