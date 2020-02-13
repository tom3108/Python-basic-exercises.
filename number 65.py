"""

time = float(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))
"""

time = float(input("Input time in seconds:"))

days = time //(24*3600)
hours = time / 3600
minutes = time / 60
months = days/30
years = months / 12

print(minutes)
print(hours)
print((days))
print(months)
print(years)
