import datetime

class Data:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def data_check(self):
        try:
            flag = datetime.datetime(self.year, self.month, self.day)
            if flag.strftime("%d") and flag.strftime("%B") and flag.strftime("%Y"):
                return flag.strftime("%d"), flag.strftime("%B"), flag.strftime("%Y")
        except BaseException:
            print("Некоректный ввод даты")
        finally:
            print("Выполнено")

    def year_check(self) -> bool:
        year = int(input("enter year: "))
        if self.year % 4 != 0 or self.year % 100 == 0 and self.year % 400 != 0:
            return False
        else:
            return True

p1 = Data(1, 6, 2018)
print(p1.data_check())
p1.year = 2020
print(p1.data_check())
print(p1.year_check())