# [17] Modules
## Smart Event Planner
======================
### 1. Random Module
======================

The random module is used to randomly select an activity from a predefined list.

*Function used:* random.choice()

*Example:*
random.choice(activities)

=====================
 2. Calendar Module
=====================

The calendar module is used to display a monthly calendar based on the year and month entered by the user.

*Function used:* calendar.month()

*Example:*
calendar.month(year, month)

=====================
### 3. OS Module
=====================

The os module is used to interact with the computer's file system. 
It checks whether folders and files exist and creates a storage folder when necessary.

*Functions used:*
- os.path.exists()
- os.mkdir()

*Example:*
os.path.exists(folder)
os.mkdir(folder)

### Mini Project: Smart Event Planner

The Smart Event Planner is a Python application that allows users to view calendars, 
generate random activity suggestions, and manage personal events.
It uses the three modules together to provide calendar generation, 
random activity selection, and automatic folder creation for storing event information.