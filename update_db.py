import MySQLdb
import os
import sys

LOCAL_DB_HOST = "localhost"
LOCAL_DB_NAME = "engage"


USER_NAME = "mania"
USER_PASSWORD = "theManiaPassword$"


QUERY_STRING = """INSERT INTO engage_video (video_name, participant_id) VALUES (%s, %s)"""

values_list = []

files = os.listdir('public/static/video')
for f in files:
	if 'mov' not in f:
		continue
	else:
		values_list.append((f, 1))

db=MySQLdb.connect(host=LOCAL_DB_HOST ,user=USER_NAME,
	                  passwd=USER_PASSWORD, db= LOCAL_DB_NAME)
c = db.cursor()

c.executemany(QUERY_STRING, values_list)
db.commit()