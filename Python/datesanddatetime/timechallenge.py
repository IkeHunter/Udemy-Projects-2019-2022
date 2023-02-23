import pytz
import datetime
import time

times = {
    0: 'Quit',
    1: {'name': 'New York City', 'zone': 'America/New_York', 'country': 'United States of America'},
    2: {'name': 'Shanghai', 'zone': 'Asia/Shanghai', 'country': 'China'},  # Peoples Republic of China
    3: {'name': 'London', 'zone': 'Europe/London', 'country': 'United Kingdom'},  # United Kingdom of Great Britain
    4: {'name': 'Istanbul', 'zone': 'Europe/Istanbul', 'country': 'Turkey'},  # Republic of Turkey
    5: {'name': 'Tokyo', 'zone': 'Asia/Tokyo', 'country': 'Japan'},  # State of Japan
    6: {'name': 'Moscow', 'zone': 'Europe/Moscow', 'country': 'Russia'},  # Russian Federation
    7: {'name': 'Dubai', 'zone': 'Asia/Dubai', 'country': 'United Arab Emirates'},
    8: {'name': 'Seoul', 'zone': 'Asia/Seoul', 'country': 'South Korea'},  # Republic of Korea (South)
    9: {'name': 'Mexico City', 'zone': 'America/Mexico_City', 'country': 'Mexico'},  # United Mexican States
    10: {'name': 'Singapore', 'zone': 'Asia/Singapore', 'country': 'Singapore'}  # Republic of Singapore
}

print()

for i in times:
    if i != 0:
        print("{}: {}, {}".format(i, times[i]['name'], times[i]['country']))
print("Or choose 0 to quit and view local and UTC time")
print("-" * 40)
while True:
    print()
    x = input("Select index of time zone to view the City's time: ")

    y = list(x)
    bool_val = True
    for i in y:
        if bool_val:
            if i in '1234567890':
                bool_val = True
            else:
                bool_val = False
                break
        else:
            break

    if (x != '') & (bool_val is True):
        x = int(x)
        if x < len(times.keys()):
            if x == 0:
                local_date_format = '%B %d, %Y'
                local_time_format = '%I:%M'

                local_date_data = datetime.datetime.now().strftime(local_date_format)
                local_time_data = datetime.datetime.now().strftime(local_time_format)

                local_zone_data = datetime.datetime.now()

                stamp_data = int(datetime.datetime.now().strftime('%H'))
                if stamp_data > 12:
                    local_stamp = 'pm'
                else:
                    local_stamp = 'am'

                print("The current date is {0}; and the local time is {1}{2}. ({3} [{4}])"
                      .format(local_date_data, local_time_data, local_stamp, time.strftime('%Z'), time.strftime('%z')))
                #  local_zone_data.tzname(), local_zone_data.strftime('%z')
                print("The current UTC time is {}".format(datetime.datetime.utcnow().strftime('%H:%M')))
                break
            country_zone = times[x]['zone']

            date_format = '%B %d, %Y'
            date_data = datetime.datetime.now(tz=pytz.timezone(country_zone)).strftime(date_format)

            time_format = '%I:%M'
            time_data = datetime.datetime.now(tz=pytz.timezone(country_zone)).strftime(time_format)

            zone_data = datetime.datetime.now(tz=pytz.timezone(country_zone))

            stamp_data = int(datetime.datetime.now(tz=pytz.timezone(country_zone)).strftime('%H'))
            if stamp_data > 12:
                stamp = 'pm'
            else:
                stamp = 'am'

            print("In {0}, {1}, the date is {2}; and the time is {3}{4}. ({5} [{6}])"
                  .format(times[x]['name'], times[x]['country'], date_data,
                          time_data, stamp, zone_data.tzname(), zone_data.strftime('%z')))
            print()
        else:
            print("Please enter lower number")
    else:
        print("Please enter index as number")
