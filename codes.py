from datetime import date, timedelta
# time delta is used to display past date.
today =date.today()
# to display date before 30 days
lastmonth = today - timedelta(days=30)
date_stamp = lastmonth.strftime("%d %B, %Y")
print(date_stamp)
