#!/usr/bin/env python
# We don't use the data provided given we already have everything from datetime library
import datetime

tot = 0
for year in xrange(1901, 2001):
    for month in xrange(1, 13):
        if datetime.date.weekday(datetime.date(year, month, 1)) == 6:
            tot += 1
print tot

# You could just instead compute 1200/7
# There are 12 * 100 first days of the month in 100 years
# 1/7 must be a Sunday, this is an approximated answer by +-1
