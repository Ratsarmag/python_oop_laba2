from datetime import datetime, timedelta

class Zate():

    def __init__(self, date):
        self.date = date
        self.date = datetime.strptime(self.date, "%Y-%m-%d")

    def getYear(self):
        return self.date.year
    
    def getMonth(self):
        return self.date.month

    def getDay(self):
        return self.date.day

    def getWeekday(self):
        return self.date.weekday()

    def getWeekdayName(self): 
        weekdayNames = {1 : "Понедельник", 2 : "Вторник", 3 : "Среда", 4 : "Четверг", 5 : "Пятница", 6 : "Суббота", 7 : "Воскресенье"}
        return weekdayNames[self.getWeekday()]

    def getMonthName(self): 
        monthNames = {
            1: 'Январь',
            2: 'Февраль',
            3: 'Март',
            4: 'Апрель',
            5: 'Май',
            6: 'Июнь',
            7: 'Июль',
            8: 'Август',
            9: 'Сентябрь',
            10: 'Октябрь',
            11: 'Ноябрь',
            12: 'Декабрь'}
        return monthNames[self.getMonth()]

class ZateExt(Zate): 
    
    def addYears(self, years): 
        self.date += timedelta(days=years * 365)

    def subtractYears(self, years): 
        self.date -= timedelta(days=years * 365)

    def addMonths(self, months): 
        self.date += timedelta(days=months * 31)

    def subtractMonths(self, months): 
        self.date += timedelta(days=months * 31)

    def addDays(self, days): 
        self.date += timedelta(days=days)

    def subtractDays(self, days): 
        self.date -= timedelta(days=days)

zate = ZateExt("2021-10-17")
zate.addYears(12)
zate.addMonths(48)
zate.subtractDays(14)

print(zate.getYear())
print(zate.getMonth())
print(zate.getDay())
print(zate.getWeekday())
print(zate.getWeekdayName())
print(zate.getMonthName())