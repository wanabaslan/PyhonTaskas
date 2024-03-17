from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        name = user["name"]
        birthday_this_year = datetime.strptime(user["birthday"], "%Y-%m-%d")
        birthday_this_year = birthday_this_year.replace(year=today.year).date()

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        if birthday_this_year.weekday() == 5:
            birthday_this_year += timedelta(days=2)
        elif birthday_this_year.weekday() == 6:
            birthday_this_year += timedelta(days=1)

        upcoming_birthdays.append((name, birthday_this_year))

    return upcoming_birthdays

users = [
    {"name": "Аліса", "birthday": "1992-03-12"},
    {"name": "Боб", "birthday": "1990-11-05"},
    {"name": "Саша", "birthday": "2005-01-13"}
]

for name, birthday in get_upcoming_birthdays(users):
    print(f"{name} святкує наступний день народження {birthday}")
