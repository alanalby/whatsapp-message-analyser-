import pandas as pd
import numpy as np
import datetime
from matplotlib import pyplot as plt
import time
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

file_name = 'message_pandas_data_frame.pkl'
df = pd.read_pickle(file_name)

df['hour'] = pd.to_datetime( df['Time'], format='%H', errors='coerce' ).dt.hour


def word_count(x):
	count=len ( x['Message'].split(' ') )
	return count-1

def letter_count(x):
	count=len ( x['Message'] )
	return count-1

df['word_count'] =  df.apply(word_count, axis=1)
df['letter_count'] =  df.apply(letter_count, axis=1)


print( df.head()  )
print( df.tail()  )

file_name = 'message_word_count_pandas_data_frame.pkl'
df.to_pickle(file_name)