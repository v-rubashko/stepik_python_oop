class HourClock:
    def __init__(self, hours):
        self.hours = hours

    def get_hours(self):
        return self._hours

    def set_hours(self, hours):
        if isinstance(hours, int) and hours in range(1, 13):
            self._hours = hours
        else:
            raise ValueError('Некорректное время')

    hours = property(get_hours, set_hours)

time = HourClock(1)

print(time.hours)
for _ in range(11):
    time.hours += 1
    print(time.hours)