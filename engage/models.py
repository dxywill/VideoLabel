from django.db import models

# Create your models here.

class Participant(models.Model):
	participant_id = models.IntegerField()
	def __str__(self):
   		return str(self.participant_id)

class Video(models.Model):
	participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
	video_name = models.CharField(max_length=50)
	def __str__(self):
   		return self.video_name

class Annotator(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
   		return self.name

class Labels(models.Model):
	video_id = models.ForeignKey(Video, on_delete=models.CASCADE)
	annotator = models.ForeignKey(Annotator, on_delete=models.CASCADE)
	engage_level = models.IntegerField()
	def __str__(self):
   		return str(self.id)