class TimePeriod:

    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes


    def __add__(self, other):
        minutes = self.minutes + other.minutes
        hours = self.hours + other.hours
        if minutes >= 60:
            minutes -= 60
            hours += 1
        return TimePeriod(hours, minutes)


    def __gt__(self, other):
        if self.hours > other.hours:
            return True
        elif self.hours < other.hours:
            return False
        elif self.minutes > other.minutes:
            return True
        else:
            return False


    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes


    def __str__(self):
        return f"{self.hours} hours, {self.minutes} minutes"


    def __getitem__(self, item):
        if item == 'hours':
            return self.hours
        elif item == 'minutes':
            return self.minutes
        else:
            raise KeyError()


if __name__ == "__main__":
    print(TimePeriod(2, 30))


""" Result:
-----------
2 hours, 30 minutes
"""