class  Time(object):

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(t1, t2):
        t3 = Time(0, 0)
        t3.hours = t1.hours + t2.hours
        t3.minutes = t1.minutes + t2.minutes
        while t3.minutes ==t3.minutes > 60:
            t3.hours = t3.hours+ 1
            t3.minutes =t3.minutes- 60
        return t3

    def displayTime(self):
        print("Time is ",self.hours,"hr",self.minutes,"m")

a = Time(2,20)
b = Time(1, 90)
c = Time.addTime(a,b)

c.displayTime()
