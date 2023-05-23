import time
import datetime
first_date1 = datetime.date(2022,10,17)
first_date2 = datetime.date(2022,12,2)
first = (first_date2 - first_date1).days + 1
second_date1 = datetime.date(2023,5,1)
second_today = datetime.date.today()
second = (second_today - second_date1).days + 1 
all = first + second
print("已經待了" + str(all) + "天")
look = input("按任意鍵繼續....")