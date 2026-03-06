import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
index = [1,2,3,4,5,6]
data = [4,67,75,45,75,46]
age = [1 ,3,6 ,-1,6,8]

detail = np.array([(data),(age)])

# print(detail)

plt.hist(age , 4)

plt.show()
