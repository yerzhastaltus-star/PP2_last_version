from datetime import datetime
def angle(now):
    minute = now.minute
    second = now.second
    second_angle = second * 6 + 0.3
    minute_angle = minute * 6 + second * 0.1
    return (minute_angle, second_angle)

class time_angle:
    def __init__(self):
        self.now = datetime.now()
        self.m_angle, self.s_angle = angle(self.now)
    def update(self):
        self.now = datetime.now()
        self.m_angle, self.s_angle = angle(self.now)
x = time_angle()
if __name__ == "__main__":
    print(x.now)
    print(x.m_angle, x.s_angle)