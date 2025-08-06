print("Statistical Testdata/30 \n-----------------")
data = [12,18,14,20,16,22,8,24,11,13,15,17,19,21,23,9,25,12,14,16,20,
        22,18,26,10,28,9,11,13,15,17,19,21,7,23,10,15,20,25,30]

sorted_data = sorted(data)
print(f"Sorted data: {sorted_data}")
print(f"Minimum: {sorted_data[0]}/30")
print(f"Maximum: {sorted_data[-1]}/30")
print(f"Range: {sorted_data[-1] - sorted_data[0]}")
mean = sum(data)/len(data)
print(f"Mean:  {mean}")

n = len(sorted_data)
median = (sorted_data[n//2] + sorted_data[(n-1) // 2])/2
print(f"Mean: {median}")

from statistics import mode
mode_value = mode(data)
#mean_value = median(data)
print(f"Mode: {mode_value}")
