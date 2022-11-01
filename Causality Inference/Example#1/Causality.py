import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# data upload
wages_occupation = pd.read_excel('Wages_Occupation.xlsx', header=0)

time = wages_occupation['year'].to_numpy().astype(int)
occupation = wages_occupation['Occupation'].to_numpy().astype(np.float32)
wage = wages_occupation['Wage'].to_numpy().astype(np.float32)

# preprocessing
min_max_scale = MinMaxScaler()
norm_wage = min_max_scale.fit_transform(wage.reshape(-1, 1))
norm_occupation = min_max_scale.fit_transform(occupation.reshape(-1, 1))

# causality study




# visualization
plt.figure()
plt.plot(time, norm_occupation, color='#d60000', linewidth=2, label='occupation')
plt.plot(time, norm_wage, color='#0e58c6', linewidth=2, label='wage')
plt.xlabel('Year')
plt.ylabel('Min-Max scaled index value')
plt.grid(color='k', alpha=0.8, linestyle='dashed', linewidth=0.5)
plt.legend(loc='best')
plt.show()
