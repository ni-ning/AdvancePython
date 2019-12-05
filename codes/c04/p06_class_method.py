# -*- coding:utf-8 -*-


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    @staticmethod
    def date_from_str(date_str):
        year, month, day = tuple(date_str.split('-'))
        return Date(int(year), int(month), int(day))

    @classmethod
    def date_from_string(cls, date_str):
        year, month, day = tuple(date_str.split('-'))
        return cls(int(year), int(month), int(day))

    def __str__(self):
        return '{year}/{month}/{day}'.format(year=self.year, month=self.month, day=self.day)


if __name__ == '__main__':
    new_day = Date(2020, 2, 20)
    new_day.tomorrow()
    print(new_day)

    date_str = '2020-12-12'
    print(Date.date_from_str(date_str))
    print(Date.date_from_string(date_str))