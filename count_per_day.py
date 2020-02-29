import pandas as pd
import numpy as np
import datetime
from matplotlib import pyplot as plt
import time

file_name = 'message_pandas_data_frame.pkl'
df = pd.read_pickle(file_name)


print(df[3000:3100])
df['Date'] = pd.to_datetime( df['Time'], format='%Y-%m-%d', errors='coerce' ).dt.floor('D')
print(df[3000:3100])


alan_df = df[(df['Name'] == ' Alan Alby')]
# print(alan_df.head().sort_values(by='Date'))
datwise_message_alan = alan_df.Date.value_counts().sort_index()

# print(datwise_message_alan)

# print(datwise_message_alan.index.)
print(datwise_message_alan.head() )




her_df = df[(df['Name'] == ' her')]
# print(alan_df.head())
datwise_message_her = her_df.Date.value_counts().sort_index()
# print(datwise_message_her)

x_per_plot = int( len(datwise_message_alan.index.tolist()) / 6 )
print(x_per_plot)
for i in range(0, 6):
	plt.subplot(2, 3, i+1)

	plt.plot(datwise_message_alan.index.tolist()[i*x_per_plot:(i+1)*x_per_plot],datwise_message_alan.tolist()[i*x_per_plot:(i+1)*x_per_plot],'b' , label='Alan')
	plt.plot(datwise_message_her.index.tolist()[i*x_per_plot:(i+1)*x_per_plot],datwise_message_her.tolist()[i*x_per_plot:(i+1)*x_per_plot] , 'r' , label='her')
	# plt.ylabel('Count')
	# plt.xlabel('Date')
	plt.xticks(rotation=90, fontsize=4)
	plt.yticks(fontsize=8)
	plt.subplots_adjust(left=.03, right=.99, top=.97, bottom=0.06)
	# plt.axis([, , 0, 750]) 
	plt.ylim((0,750))
# plt.figure()
plt.show()
# plt.savefig('Count_per_day.png', bbox_inches='tight',dpi=1000)


# plt.plot(datwise_message_her.index.tolist(),datwise_message_her.tolist() , 'r')
# plt.title('her Message Count')
# plt.ylabel('Count')
# plt.xlabel('Date')
# plt.show()




# df.insert(2, "Date", [21, 23, 24, 21], True). 