# # if using dates and not just times, than date-time module is better to use than time module
# import time
#
# print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))
#
# print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))
#
# if time.daylight != 0:
#     print("\tDaylight Saving TIme is in effect for this location")
#     print("\tThe DST timezone is " + time.tzname[1])
#
# print("Local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# print("UTC time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))

import datetime

print(datetime.datetime.today())  # does now allow timezone specification
print(datetime.datetime.now())  # allows timezone specification
print(datetime.datetime.utcnow())
