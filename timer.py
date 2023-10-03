import datetime
from datetime import timedelta
 
datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
date1 = '2020-01-10 17:51:28.585'
date2 = datetime.datetime.now()
diff = datetime.datetime.strptime(str(date2), datetimeFormat)\
    - datetime.datetime.strptime(str(date1), datetimeFormat)
 
print("Difference:", diff)
print("Days:", diff.days)
print("Microseconds:", diff.microseconds)
print("Seconds:", diff.seconds)
import datetime
old_time = datetime.datetime.now()
a=old_time.strftime('%Y-%m-%d %H:%M:%S.%f')
print("hello"+a)
new_time = old_time - datetime.timedelta(hours=2, minutes=10)
print(new_time)
