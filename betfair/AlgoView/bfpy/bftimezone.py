#!/usr/bin/env python
# -*- coding: latin-1; py-indent-offset:4 -*-
################################################################################
# 
# This file is part of BfPy
#
# BfPy is a Python library to communicate with the Betfair Betting Exchange
# Copyright (C) 2010 Daniel Rodriguez (aka Daniel Rodriksson)
# Copyright (C) 2011 Sensible Odds Ltd.
#
# You can learn more and contact the author at:
#
#    http://code.google.com/p/bfpy/
#
# BfPy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BfPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BfPy. If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
'''
BfPy Timezone classes. Adapted (if needed) from the Python documentation to make
them more generic
'''

import calendar
from datetime import datetime, timedelta, tzinfo
import time as _time

import bfglobals


ZERO = timedelta(0)


class UTC(tzinfo):
    '''
    UTC timezone.
    '''
    def utcoffset(self, dt):
        '''
        Return the offset to UTC (GMT) for the given datetime

        @param dt: datetime to see offset against
        @type dt: datetime
        '''
        return ZERO

    def tzname(self, dt):
        '''
        Return the name of this timezone for the given datetime

        @param dt: datetime to see offset against
        @type dt: datetime
        '''
        return "UTC"

    def dst(self, dt):
        '''
        Return the daylight savings offset for the given datetime

        @param dt: datetime to see offset against
        @type dt: datetime
        '''
        return ZERO


class LocalTimezone(tzinfo):
    '''
    System specific local timezone.

    As seen in the Python docs (with mods)
    '''
    def __init__(self):
        self.stdOffset = timedelta(seconds=-_time.timezone)
        if _time.daylight:
            self.dstOffset = timedelta(seconds=-_time.altzone)
        else:
            self.dstOffset = self.stdOffset

        self.dstDiff = self.dstOffset - self.stdOffset

    def utcoffset(self, dt):
        '''
        Return the offset to UTC (GMT) for the given datetime

        @param dt: datetime to see offset against
        @type dt: datetime
        '''
        return self.dstOffset if self._isdst(dt) else self.stdOffset

    def dst(self, dt):
        '''
        Return the daylight savings offset for the given datetime

        @param dt: datetime to see offset against
        @type dt: datetime
        '''
        return self.dstDiff if self._isdst(dt) else ZERO

    def tzname(self, dt):
        '''
        Return the name of this timezone for the given datetime

        @param dt: datetime to see offset against
        @type dt: datetime
        '''
        return _time.tzname[self._isdst(dt)]

    def _isdst(self, dt):
        '''
        Private function to find out if the system reports
        to be in DST mode for the given datetime

        @param dt: datetime to see offset against
        @type dt: datetime
        '''
        tt = (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.weekday(), 0, -1)
        stamp = _time.mktime(tt)
        tt = _time.localtime(stamp)
        return tt.tm_isdst > 0


def localizeDateTime(dt):
    '''
    Given a datetime.datetime instance it localizes the time to the local system
    (according to bfglobals settings) and adds a timezone object if needed
    '''
    if bfglobals.timeUtc or bfglobals.timeUtcIn:
        # Calling application wants utc
        tmpdt = dt if not bfglobals.timeReturnAware else dt.replace(tzinfo=UTC())
        return tmpdt

    # Localized time wished
    localTimezone = LocalTimezone()
    try:
        utcoffset = localTimezone.utcoffset(dt)
    except:
        # Fails with the dates from getSubscriptionInfo
        # Generate an offset for our current time
        utcoffset = localTimezone.utcoffset(datetime.now())

    tmpdt = dt + utcoffset

    if bfglobals.timeReturnAware:
        tmpdt = tmpdt.replace(tzinfo=localTimezone)

    return tmpdt


def unLocalizeDateTime(dt):
    '''
    Given a datetime.datetime instance it unlocalizes it (according to bfglobals settings)
    and honours a timezone object if needed
    '''
    if bfglobals.timeUtc or bfglobals.timeUtcOut:
        # Calling application is passing utc
        return dt.replace(tzinfo=None)
        
    utcoffset = ZERO
    if bfglobals.timeHonourAware:
        utcoffset = None if dt.tzinfo is None else dt.utcoffset()

    if not bfglobals.timeHonourAware or utcoffset is None:
        localTimezone = LocalTimezone()
        try:
            utcoffset = localTimezone.utcoffset(dt)
        except:
            # Fails with the dates from getSubscriptionInfo
            # generate an offset for our current time
            utcoffset = localTimezone.utcoffset(datetime.now())

    return dt - utcoffset


def parseDateTimeString(dtString):
    '''
    Parses an incoming datetime string and returns a datetimeobject
    (localized or not according to preferences)
    '''
    # Bf time is: 2000-01-01T00:00:00.000Z
    dtParts = dtString.split('.')
    dt = datetime.strptime(dtParts[0], '%Y-%m-%dT%H:%M:%S')
    dt = dt.replace(microsecond=int(dtParts[1][0:3]) * 1000)

    return localizeDateTime(dt)
    

def fromTimestamp(ts):
    '''
    Parses an incoming timestamp and returns a datetimeobject
    (localized or not according to preferences)
    '''
    if not bfglobals.timeConvertTimestamps:
        return ts

    secs, msecs = divmod(ts, 1000)

    dt = datetime.utcfromtimestamp(secs)
    dt = dt.replace(microsecond=msecs * 1000)
    return localizeDateTime(dt)


def fromTimestampString(tstamp):
    '''
    Parses an incoming timestamp string and returns a datetimeobject
    (localized or not according to preferences)
    '''
    ts = long(tstamp)
    return fromTimestamp(ts)


def getDateTimeNow():
    '''
    Returns the current time either in local time or utc
    according to the preferences in bfglobals. This datetime
    object is meant to be sent to the API servers
    '''
    if bfglobals.timeUtc or bfGlobals.timeUtcOut:
        return datetime.utcnow()

    return datetime.now()
    

def getDateTime(*args):
    '''
    Constructs an internal datetime object to be sent to the
    API servers unlocalized if so set in the bfglobals
    '''
    dt = datetime(*args)
    return unLocalizeDateTime(dt)
