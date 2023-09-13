import datetime
from datetime import date, timedelta, timezone

import pytz


# todo test this shit out
def convert_us_datetime_to_date_object(us_datetime: str) -> date:
    full_date, t = us_datetime.split(' ')

    year, month, day = list(map(int, full_date.split('-')))

    hour, *_ = t.split(':')

    if int(hour) + 3 >= 24: # convert to moscow timezone
        day += 1
        hour = int(hour) + 3 - 24

    return date(year, month, day)

def convert_ru_date_to_timestamp(ru_date: date, include_last_day: bool = False) -> int:
    ru_date = datetime.datetime.fromordinal(ru_date.toordinal())

    if include_last_day:
        ru_date += timedelta(days=1) - timedelta(seconds=1)

    return int(ru_date.timestamp() * 1000) # convert to milliseconds timestamp

def convert_utc_timestamp_to_ru_date(utc_timestamp: int) -> date:
    dt = datetime.datetime.fromtimestamp(utc_timestamp)
    return dt.date()
