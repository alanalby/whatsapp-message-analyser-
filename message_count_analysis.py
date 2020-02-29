import pandas as pd
import numpy as np
import datetime
from matplotlib import pyplot as plt
import time
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

file_name = 'message_word_count_pandas_data_frame.pkl'
df = pd.read_pickle(file_name)


alan_df = df[(df['Name'] == ' Alan Alby')]
# alan_df.set_index('hour',inplace=True)

# datwise_message_alan = alan_df.hour.value_counts().sort_index()
# print(datwise_message_alan.head() )


her_df = df[(df['Name'] == ' her')]
# datwise_message_her = her_df.hour.value_counts().sort_index()
# print(datwise_message_her.head() )


# x_per_plot = int( len(datwise_message_alan.index.tolist()) / 6 )

# plt.plot(datwise_message_her.index.tolist(),datwise_message_her.tolist() , 'r')
# plt.plot(datwise_message_alan.index.tolist(),datwise_message_alan.tolist() , 'b')
# plt.ylabel('Count')
# plt.xlabel('Time')
# plt.show()

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

start_date = alan_df.Time.min()
end_date = alan_df.Time.max()

start_date = start_date.replace(minute=00, hour=00, second=00)

total_month = diff_month(end_date,start_date)


month_list = []
alan_monthly_message_list = []
her_monthly_message_list = []



delta =relativedelta(months=+6)
month_delta = relativedelta(months=+1)
while start_date <= end_date:
	i = 1
	figure_start_date = start_date
	figure_end_date = start_date + delta
	while figure_start_date < figure_end_date:
		
		
		month_start_date = figure_start_date
		month_end_date = figure_start_date + month_delta
		# print(month_start_date)
		# print(month_end_date)
		month_alan_mask = ( alan_df['Time'] <= month_end_date ) & ( alan_df['Time'] >= month_start_date )
		month_alan_df = alan_df.loc[month_alan_mask]
		datwise_message_count_alan = []

		for x in range(1,25):
			datwise_message_count_alan.append(sum(month_alan_df.loc[month_alan_df['hour']==x].word_count))
		# datwise_message_alan = month_alan_df.hour.value_counts().sort_index()

		month_her_mask = ( her_df['Time'] <= month_end_date ) & ( her_df['Time'] >= month_start_date )
		month_her_df = her_df.loc[month_her_mask]
		datwise_message_her = month_her_df.hour.value_counts().sort_index()
		datwise_message_count_her = []
		for x in range(1,25):
			datwise_message_count_her.append(sum(month_her_df.loc[month_her_df['hour']==x].word_count))


		#plot1
		plt.subplot(2, 3, i)

		plt.title(month_start_date.strftime('%B:%Y'))
		plt.ylabel('Message Count')
		
		# plt.xlabel('Hour')
		# plt.plot(np.arange(1,25),datwise_message_count_alan , 'b')
		# plt.plot(np.arange(1,25),datwise_message_count_her , 'r')
		# plt.xticks( fontsize=8)
		# plt.yticks(fontsize=8)
		# plt.subplots_adjust(left=.04, right=.98, top=.96, bottom=0.06)
		# plt.ylim((0,10000))
		# plt.xlim((0,24))
		

		#plot2
		# [float(x)-.5 for x in datwise_message_her.index.tolist()]
		# ax = plt.subplot(2, 3, i)
		# ax.bar( np.arange(1,25),datwise_message_count_alan, color = 'b', width = 0.5)
		# ax.bar([float(x)-.5 for x in np.arange(1,25)],datwise_message_count_her, color = 'r', width = 0.5)
		# ax.legend(labels=['Alan', 'her'])
		# ax.set_title(month_start_date.strftime('%B:%Y'))
		# ax.set_ylabel('Message Count')
		# ax.set_xlabel('hour')

		#plot3
		alan_total = sum(datwise_message_count_alan)
		her_total = sum(datwise_message_count_her)
		labels = 'Alan', 'her'
		explode = (0.01, 0.01)
		ax = plt.subplot(2, 3, i)
		ax.set_title(month_start_date.strftime('%B:%Y') + ' message count')
		sizes = [alan_total,her_total]
		ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
		ax.axis('equal')


		# print(month_alan_df.head())
		# print(month_alan_df.head())
		# month_list.append(month_start_date.strftime('%B:%Y'))
		# alan_monthly_message_list.append(sum(month_alan_df.word_count ))
		# her_monthly_message_list.append(sum(month_alan_df.word_count ))


		figure_start_date = month_end_date
		i +=1
	plt.show()


	start_date += delta


# print(month_list)
# print(alan_monthly_message_list)
# print(her_monthly_message_list)

# def func(pct, allvals):
#     absolute = int(pct/100.*np.sum(allvals))
#     return "{:.1f}%\n({:d} g)".format(pct, absolute)


# fig1, ax = plt.subplots(2, 1)
# fig1.subplots_adjust(0.3, 0, 1, 1)
# fig1.suptitle('Message count', fontsize=16 , y=0.98 , x =0.1)






# ax[0].set_title('Alan', y=0.4 , x =0.8)
# ax[0].pie(alan_monthly_message_list , autopct='%1.1f%%', shadow=False, startangle=90)
# total = sum(alan_monthly_message_list)
# ax[0].legend( loc='upper left', labels=['%s, %1.1f%%' % ( l, (float(s) / total) * 100) for l, s in zip(month_list, alan_monthly_message_list)], prop={'size': 11},  bbox_transform=fig1.transFigure)
# ax[0].axis('equal')




# # ax = plt.subplot(1, 2, 2)
# ax[1].set_title('her', y=0.4 , x =0.8)
# ax[1].pie(her_monthly_message_list , autopct='%1.1f%%', shadow=False, startangle=90)
# total = sum(her_monthly_message_list)
# ax[1].legend( loc='lower left', labels=['%s, %1.1f%%' % ( l, (float(s) / total) * 100) for l, s in zip(month_list, her_monthly_message_list)], prop={'size': 11},  bbox_transform=fig1.transFigure)
# ax[1].axis('equal')


# plt.show()





