import pandas as pd
import numpy as np

message_file  = open("her.txt", "rt")
message_data  = message_file.read()
# print(message_data[0:2000])

# sample = message_data[0:2000]
message_data_list = np.array( message_data.split('\n')[1:] )
# print(message_data_list)
data = []
for message in message_data_list:
	try:
		temp_data = []
		individual_message_list = message.split('-',1)
		# print(individual_message_list)
		temp_data = [ pd.to_datetime(individual_message_list[0] , format='%d/%m/%y, %I:%M %p ' ) ] + individual_message_list[1].split(':',1)
		
		if len(temp_data) ==3:
			data.append(temp_data)
		else:
			print(temp_data)
		# print(temp_data)
	except Exception as e:
		# print(e)
		# break
		pass

# print(data)
print(len(data))
df = pd.DataFrame(data,columns=['Time','Name','Message'])
# print(df)
file_name = 'message_pandas_data_frame.pkl'
df.to_pickle(file_name)

# df = pd.read_pickle(file_name)