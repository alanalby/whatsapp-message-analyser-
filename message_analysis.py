import pandas as pd
import numpy as np
import datetime
from matplotlib import pyplot as plt

file_name = 'message_pandas_data_frame.pkl'
df = pd.read_pickle(file_name)
alan_count = len ( df[(df['Name'] == ' Alan Alby')] )
her_count = len ( df[(df['Name'] == ' her')] )


print(alan_count)
print(her_count)

plt.plot([1,2,3],[4,5,1])
plt.show()

# date_time_str = '2018-06-29 08:15:27.243860'
# date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
# print(date_time_obj)