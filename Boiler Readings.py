import re
import statistics
from functools import reduce
readings = [["20.5", "30.1", "50.5", "37.5"],
["19.1", "32.4", "45.6", "12.5a"],
["18.2", "29.3", "-10.2", "19.5"],
["12.6", "15.2", "20.5", "22.4"],
["21.4", "-0", "20.5", "23.1]"],
["34.3", "33.3", "20.5", "19.5"],
["-a.23", "56.1", "30.2", "19.9"]]

# Your code goes here
curated_readings = []
for daily_readings in readings:
    filtered_readings = list(map(float,filter(lambda x: bool(re.match(r'^(\d+\.\d)$', x)), daily_readings)))
    print("\n",filtered_readings)
    curated_readings.append(filtered_readings)
avg_reading = list(map(lambda daily_readings : statistics.mean(daily_readings), curated_readings))

print("\n",avg_reading)

#avg_readings = list(map(lambda daily_readings : statistics.mean(daily_readings), filtered_readings))
#print(avg_readings)