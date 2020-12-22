"""Given a clock time in hh:mm format, determine, to the nearest degree, the
angle between the hour and the minute hands.Bonus: When, during the course of a
day, will the angle be zero?"""


def get_angle(hour, minute):
    hour = 0 if hour == 12 else hour

    minute_degrees = minute*6
    hour_degrees = 0.5*(60*hour + minute)

    difference = abs(hour_degrees - minute_degrees)
    acute_angle = min(360 - difference, difference)

    return acute_angle


hour = int(input("Enter the hour: "))
minute = int(input("Enter the mimutes: "))
print(f'{hour}:{minute} = {get_angle(hour, minute)}')
assert get_angle(5, 50) == 125
