import os
from subprocess import call
import time

openface_exe = '/Users/xinyi/Developer/openface/OpenFace/bin/FeatureExtraction'

video_folder = '/Users/xinyi/research/engage/emotion/public/static/video/'
output_folder = video_folder + 'csv/'
files = os.listdir('public/static/video')
for f in files:
	if 'mp4' not in f:
		continue
	else:
		command_to_run = openface_exe + ' -f ' +  video_folder + f + ' -of ' + output_folder + f[0:-4] + '.csv'
		print(command_to_run)
		os.system(command_to_run)
		time.sleep(20)
