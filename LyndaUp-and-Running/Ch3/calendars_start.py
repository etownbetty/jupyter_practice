#
# Example file for working with Calendars
#

import calendar as cal

c = cal.TextCalendar(cal.SUNDAY)
#str = c.formatmonth(2016, 1, 0, 0)

#print str

# create an HTML formatted calendar
#hc = cal.HTMLCalendar(cal.SUNDAY)
#str = hc.formatmonth(2016, 1)
#print str

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
#for i in c.itermonthdays(2016, 8):
#  print i

# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
#for name in cal.month_name:
#  print name

#for day in cal.day_name:
#  print day

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
for m in range(1,13):
  # returns an array of weeks that represent the month
  calen = cal.monthcalendar(2016, m)
  # The first Friday has to be within the first two weeks
  weekone = calen[0]
  weektwo = calen[1]

  if weekone[cal.FRIDAY] != 0:
    meetday = weekone[cal.FRIDAY]
  else:
    # if the first friday isn't in the first week, it must be in the second
    meetday = weektwo[cal.FRIDAY]

  print "%10s %2d" % (cal.month_name[m], meetday)








