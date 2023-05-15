import numpy as np
import pandas as pd

data = pd.read_csv("testData5.txt", names=['detected', 'actual', 'zone'])
print(data)

single = data[(data['zone'] < 6) | ((data['zone'] >= 11) & (data['zone'] <= 15))]
triple = data[(data['zone'] >= 6) & (data['zone'] <= 10)]
double = data[(data['zone'] >= 16)]

single_count = single.shape[0]
single_correct_count = np.where(single.detected == single.actual)[0].size

double_count = double.shape[0]
double_correct_count = np.where(double.detected == double.actual)[0].size

triple_count = triple.shape[0]
triple_correct_count = np.where(triple.detected == triple.actual)[0].size

data2 = pd.read_csv("testData4.txt", names=['detected', 'actual', 'zone'])
print(data2)
correct = np.where(data2.detected == data2.actual)[0]
print(correct.size)