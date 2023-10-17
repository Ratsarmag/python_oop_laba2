from datetime import datetime

class Period(): 

    def __init__(self, time1, time2):
        self.time1 = time1
        self.time2 = time2

    def getSeconds(self):
        time1_dt = datetime.strptime(self.time1, "%Y-%m-%d %H:%M:%S")
        time2_dt = datetime.strptime(self.time2, "%Y-%m-%d %H:%M:%S")
        diff = time1_dt - time2_dt
        return diff.total_seconds()

    def getMinutes(self):
        return self.getSeconds() // 60

    def getHours(self): 
        return self.getMinutes() // 60

    def getDays(self): 
        return self.getHours() // 24

period = Period("2023-10-17 16:23:11", "2023-06-26 13:48:00")

print(period.getSeconds())
print(period.getMinutes())
print(period.getHours())
print(period.getDays())
