import statistics
from functools import reduce
data = [1.3,2.7,0.8,4.1,4.3,-0.1]

above_avg_data = list (filter(lambda x: x > statistics.mean(data) , data))

print(above_avg_data)

add = lambda x,y: x+y
sum = reduce(add,above_avg_data)
print(sum)

