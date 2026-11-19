import random
import calendar
import os

print("=== SMART EVENT PLANNER ===")

folder = "My Events"
filename = folder + "/events.txt"

if not os.path.exists(folder):
    os.mkdir(folder)

if not os.path.exists(filename):
    open(filename, "w").close()

activities = [
    "Study Session",
    "Movie Night",
    "Sports Day",
    "Family Gathering",
    "Game Night",
    "Reading Time",
    "Outdoor Adventure",
    "Group Project"
]

while True:
    print("\n=== MAIN MENU ===")
    print("[1] View Calendar")
    print("[2] Random Activity")
    print("[3] Add Event")
    print("[4] View Events")
    print("[5] Delete All Events")
    print("[6] Exit")

    choice = input("\nChoose an option: ")

    match choice:
        case "1":
            year = int(input("Enter year: "))
            month = int(input("Enter month (1-12): "))

            if 1 <= month <= 12:
                print(calendar.month(year, month))
            else:
                print("Invalid month!")

        case "2":
            print("\nSuggested Activity:")
            print(random.choice(activities))

        case "3":
            event = input("Enter event name: ")
            date = input("Enter event date (MM/DD/YYYY): ")

            with open(filename, "a") as file:
                file.write(date + " - " + event + "\n")

            print("Event successfully saved!")

        case "4":
            with open(filename, "r") as file:
                events = file.read()

            if events:
                print("\n=== YOUR EVENTS ===")
                print(events)
            else:
                print("No events found.")

        case "5":
            confirm = input("Delete all events? (yes/no): ")

            if confirm.lower() == "yes":
                open(filename, "w").close()
                print("All events deleted!")
            else:
                print("Deletion cancelled.")

        case "6":
            print("Thank you for using Smart Event Planner!")
            break

        case _:
            print("Invalid choice. Please try again.")