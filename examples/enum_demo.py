from datetime import date
from enum import Flag


class Weekday(Flag):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    @classmethod
    def from_date(cls, date):
        return cls(date.isoweekday())


if __name__ == "__main__":
    print(Weekday.from_date(date.today()))
    chores_for_ethan: dict[str, Weekday] = {
        "feed the cat": Weekday.MONDAY | Weekday.WEDNESDAY | Weekday.FRIDAY,
        "do the dishes": Weekday.TUESDAY | Weekday.THURSDAY,
        "answer SO questions": Weekday.SATURDAY,
    }
    print(type(chores_for_ethan))
