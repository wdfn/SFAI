from django.db import models
from django.forms import ModelForm
from django import forms

class Student(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)

	def __str__(self):
		return self.first_name + self.last_name

class Submission(models.Model):
	student = models.ForeignKey(Student)
	description = models.CharField(max_length=1000)
    attachment = forms.FileField()
	submission_date = models.DateTimeField('date submitted')
	#add the database interaction stuff here 

class Event(models.Model):
	event_name = models.CharField(max_length=200)
	event_description = models.CharField(max_length=1000)
	exhibition_date = models.DateTimeField('exhibition date')
	deadline_date = models.DateTimeField('deadline date')
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


class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = '__all__'
    