import random
from datetime import datetime, timedelta
date1_str = input("Enter first date (in YYYY-MM-DD format): ")
date2_str = input("Enter a second date (in the format YYYY-MM-DD): ")
date1 = datetime.strptime(date1_str, "%Y-%m-%d")
date2 = datetime.strptime(date2_str, "%Y-%m-%d")
days_between = (date2 - date1).days
new_date = date1 + timedelta(days=random.randint(1, days_between))
if new_date.weekday() == 0:
    print("I have no vinaigrette!")
else:
    print(f"The new date is:{new_date.strftime('%Y-%m-%d')}")
