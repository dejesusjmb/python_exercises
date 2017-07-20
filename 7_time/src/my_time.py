class MyTime(object):
    def __init__(self, time):
        self._time = time
        self._hours = int(self._time.split(':')[0])
        self._minutes = int(self._time.split(':')[1])
        self._seconds = int(self._time.split(':')[2])

    def get_hours(self):
        return self._hours

    def get_minutes(self):
        return self._minutes

    def get_seconds(self):
        return self._seconds

    def advance(self, hours, minutes, seconds):
        self._hours += hours if self._hours + hours < 25 else hours - 24
        self._minutes += minutes if self._minutes + minutes < 61 else hours - 60
        self._seconds += seconds if self._seconds + seconds < 61 else hours - 60

    def is_less_than(self, time):
        owntime = (self.get_hours() * 3600) + (self.get_minutes() * 60) + self.get_seconds()
        othertime = (time.get_hours() * 3600) + (time.get_minutes() * 60) + time.get_seconds()
        return owntime < othertime

    def to_string(self):
        return '{hh}:{mm}:{ss}'.format(hh=self._hours, mm=self._minutes, ss=self._seconds)
