import json
from datetime import datetime

FILENAME = "birthdays.json"

def load_birthdays():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_birthdays(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)

def check_today_birthdays(birthdays):
    today = datetime.today().strftime("%d-%m")
    for name, bdate in birthdays.items():
        if bdate == today:
            print(f" Today is {name}'s Birthday!")

def add_birthday():
    name = input("Enter person's name: ")
    date = input("Enter birthday (DD-MM): ")
    birthdays = load_birthdays()
    birthdays[name] = date
    save_birthdays(birthdays)
    print(" Birthday saved!")

birthdays = load_birthdays()
check_today_birthdays(birthdays)

if input("Do you want to add a new birthday? (y/n): ").lower() == 'y':
    add_birthday()
