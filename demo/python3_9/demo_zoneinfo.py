import zoneinfo
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from typing import Set, List


def print_available_timezones() -> None:
    available_timezones: Set[str] = zoneinfo.available_timezones()
    sorted_timezones: List[str] = sorted(available_timezones)
    for tz in sorted_timezones:
        print(tz)


def print_time_info() -> None:
    utc_time: datetime = datetime.now(timezone.utc)
    print(utc_time)

    utc_time_aware: datetime = utc_time.replace(tzinfo=timezone.utc)
    print(utc_time_aware)

    tz_asia_seoul: ZoneInfo = ZoneInfo("Asia/Seoul")
    seoul_time: datetime = utc_time_aware.astimezone(tz_asia_seoul)
    print(seoul_time)


if __name__ == "__main__":
    print_time_info()
