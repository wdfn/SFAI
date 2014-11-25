from django.db import models

class Student(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)

	def __str__(self):
		return self.first_name + self.last_name

class Submission(models.Model):
	student = models.ForeignKey(Student)
	description = models.CharField(max_length=1000)
	submission_date = models.DateTimeField('date submitted')
	#add the database interaction stuff here 

class Events(models.Model):
	event_name = models.CharField(max_length=200)
	event_description = models.CharField(max_length=1000)
	num_submissions = 0
	max_num_submissions = models.IntegerField(default=1000)
	
	def __str__(self):
		return self.event_name
	
	def submit(self):
		self.num_submissions += 1
		if self.num_submissions < max_num_submissions:
			return True
		else:
			return False


