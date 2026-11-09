from math import floor, ceil
import re

HM_DIST = 21.0975
FM_DIST = 42.195

distances = {
    "5k": 5,
    "10k": 10,
    "half": HM_DIST,
    "full": FM_DIST,
}

class Time:
    def __init__(self, hours: int, mins: int, secs: int):
        if secs > 60:
            n = floor(secs/60)
            mins += n
            secs -= n * 60

        if mins > 60:
            n = floor(mins/60)
            hours += n
            mins -= n * 60

        self.hours = hours
        self.mins = mins
        self.secs = secs

    def to_secs(self):
        return 3600 * self.hours + 60*self.mins + self.secs

    def __repr__(self):
        if self.hours == 0:
            return f"{self.mins}m {self.secs}s"
        return f"{self.hours}h {self.mins}m {self.secs}s"

def from_secs(secs):
    hours = floor(secs / 3600)
    secs -= hours*60*60
    mins = floor(secs / 60)
    secs -= mins*60
    secs = floor(secs)
    return Time(hours, mins, secs)

def time_per_k(time, dist):
    time = time.to_secs() / dist
    return from_secs(time)


def from_str(s):
    assert bool(re.fullmatch(r"[0-9 ]+", s))
    x = s.split()
    x = [int(i) for i in x]
    assert len(x) <= 3
    x += [0]*(3-len(x))

    return Time(*x)
