# -*- coding:utf-8 -*-


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    @staticmethod
    def date_from_str():
    

    def __str__(self):
        return '{year}-{month}-{day}'.format(year=self.year, month=self.month, day=self.day)


if __name__ == '__main__':
    new_day = Date(2020, 2, 20)
    new_day.tomorrow()
    print(new_day)
