import datetime
import pytz

# DATE
# year, month and day
d = datetime.date(2016, 7, 24)      # 07 give us a syntax error
print(d)

# current local date
tday = datetime.date.today()
print(tday)

# grap just the year, month or day
print(tday.year)
print(tday.month)
print(tday.day)
print(tday.weekday())           # monday 0 sunday 6
print(tday.isoweekday())        # monday 1 sunday 7

# the date will be one week from now
tdelta = datetime.timedelta(days=7)
print(tday + tdelta)
# one week ago
print(tday - tdelta)

# get the current age
birthday = datetime.date(1977, 10, 20)
current_age = tday - birthday
print(current_age.days)
print(current_age.total_seconds())

# TIME
# hours, minutes, seconds and microseconds

# create a new local time
t = datetime.time(9, 30, 45, 100000)
print(t.hour)

# most of the time, time of the day and date are needed
dt = datetime.datetime(2016, 7, 24, 9, 30, 45, 100000)
print(dt)

# I can grap the date and time
print(dt.date())
print(dt.time())
print(dt.year)
print(dt + tdelta)

print('=====')
dt_today = datetime.datetime.today()        # current local datetime with a timezone of none
dt_now = datetime.datetime.now()            # gives us an option to pass in a timezone
dt_utcnow = datetime.datetime.utcnow()      # current UTC time TZ info is still none
print(dt_today)
print(dt_now)
print(dt_utcnow)

# using pytz module
dt = datetime.datetime(2016, 7, 24, 9, 30, 45, 100000, tzinfo=pytz.UTC)     # +00:00 on the end, UTC offset
print(dt)

# get the current UTC time, that is also timezone aware
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)


dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
dt_ist = dt_utcnow.astimezone(pytz.timezone('Europe/Istanbul'))
print(dt_ist)

# print(pytz.all_timezones)       # all timezone list

# make a naive datetime timezone aware
# create a new local datetime that does not have timezone information
dt_tr = datetime.datetime.now()
print(dt_tr)

# convert this to Istanbul timezone
# first run the timezone localize function
ist_tz = pytz.timezone('Europe/Istanbul')
dt_tr = ist_tz.localize(dt_tr)      # now it is timezone aware
print(dt_tr)

# now convert this to datetime
dt_berlin = dt_tr.astimezone(pytz.timezone('Europe/Berlin'))
print(dt_berlin)

# datetime in a specific format
print(dt_berlin.strftime('%B, %d, %Y'))
# a list of all the format codes
# https://docs.python.org/3/library/datetime.html

# convert a string to datetime
dt_str = 'May, 24, 2021'
dt = datetime.datetime.strptime(dt_str, '%B, %d, %Y')
print(dt)

# strftime - Datetime to String
# strptime - String to Datetime
