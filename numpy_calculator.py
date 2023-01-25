from http.client import CONTINUE
from pickle import FALSE, TRUE
import numpy as np
numbers = [0,1,2,3,4,5,6,7,8]
print(len(numbers))
try:
    if len(numbers) < 9: 
        raise ValueError
except ValueError:
    print("List must contain nine numbers.")
    pass       

stat_values = {1:[],
0: [], 
'variance': [],
1: [],
4:[], 
3:[]}
#numbers_list = numbers.split()
numbers_matrix = np.array(numbers)
numbers_reshaped = numbers_matrix.reshape(3,3)
stats = list(stat_values.values())
print(numbers_reshaped)
std_rows = np.std(numbers_reshaped, axis=0)
std_columns = np.std(numbers_reshaped,axis=1) 
std_flattened = np.std(numbers_reshaped)

stats[0].append(std_rows)
stats[0].append(std_columns)
stats[0].append(std_flattened)

mean_rows = np.mean(numbers_reshaped, axis=0)
mean_columns = np.mean(numbers_reshaped,axis=1) 
mean_flattened = np.mean(numbers_reshaped)

stats[1].append(mean_rows)
stats[1].append(mean_columns)
stats[1].append(mean_flattened)

var_rows = np.var(numbers_reshaped, axis=0)
var_columns = np.var(numbers_reshaped,axis=1) 
var_flattened = np.var(numbers_reshaped)

stats[2].append(var_rows)
stats[2].append(var_columns)
stats[2].append(var_flattened)

max_rows = np.amax(numbers_reshaped, axis=0)
max_columns = np.amax(numbers_reshaped,axis=1) 
max_flattened = np.amax(numbers_reshaped)

stats[3].append(max_rows)
stats[3].append(max_columns)
stats[3].append(max_flattened)

min_rows = np.amin(numbers_reshaped, axis=0)
min_columns = np.amin(numbers_reshaped,axis=1) 
min_flattened = np.amin(numbers_reshaped)

stats[4].append(min_rows)
stats[4].append(min_columns)
stats[4].append(min_flattened)

print(stats)