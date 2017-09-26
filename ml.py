# LSTM for sequence classification in the IMDB dataset
import numpy as np
import pandas as pd
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
# fix random seed for reproducibility

import _mysql
np.random.seed(7)

LOCAL_DB_HOST = "localhost"
LOCAL_DB_NAME = "engage"

USER_NAME = "mania"
USER_PASSWORD = "theManiaPassword$"

QUERY_STRING = """SELECT engage_labels.id AS label_id, engage_level, video_name
 FROM engage_labels INNER JOIN engage_video ON engage_labels.video_id_id = engage_video.id """


def load_data():
	# get labels from database
	y = list(range(111))
	names = []
	db=_mysql.connect(host=	LOCAL_DB_HOST ,user=USER_NAME,
	                  passwd=USER_PASSWORD, db= LOCAL_DB_NAME)

	db.query(QUERY_STRING)
	r=db.store_result()
	res = r.fetch_row(maxrows=0, how=1)
	for r in res:
		label_id = int(r['label_id'])
		engage_level = int(r['engage_level'])
		video_name = r['video_name'].decode('utf-8')
		idx = video_name.split('-')[1].split('.')[0]
		y[int(idx)] = engage_level

	y = y[0:-1]
	#print(y)
	# get X
	file_name = '107.csv'
	df=pd.read_csv('107.csv', sep=',',header=0, dtype=np.float64)
	values = df.values
	interval = int((34812 / 1102.0) * 10)

	x = []
	for i in range(111):
		start = interval * i
		end = interval * (i + 1)
		temp_l = []
		if end < 34812:
			for j in range(start, end):
				temp_l.append(values[j][4:])
			x.append(temp_l)

	# Delete invalid data
	for i, item in enumerate(y):
		if y[i] == 4:
			del y[i]
			del x[i]
		else:
			y[i] = y[i] - 1
	return (y, x)

y, X = load_data()


model = Sequential()
model.add(LSTM(32, input_shape=(315, 427)))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())
model.fit(X, y, nb_epoch=3, batch_size=10)
# Final evaluation of the model
# scores = model.evaluate(X_test, y_test, verbose=0)
# print("Accuracy: %.2f%%" % (scores[1]*100))
