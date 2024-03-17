from datetime import datetime

def get_days_from_today(date):
    today = datetime.today().strftime("%Y-%m-%d")
    date_format = datetime.strptime(date, "%Y-%m-%d")
    today_format = datetime.strptime(today, "%Y-%m-%d")
    result = today_format - date_format
    return f"{result.days} дней"
    

print(get_days_from_today("2024-02-28"))


