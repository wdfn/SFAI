from django.shortcuts import render
import datetime
from django.http import HttpResponse
from django.template import RequestContext, loader
from portal.models import Submission

# from polls.models import Question


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
	return render(request, 'index.html')

def submitted(request):
    print 'RECEIVED REQUEST: ' + request.method
    s = Submission()
    s.username =  request.POST['username']
    s.name = request.POST['full_name']
    s.file_url = request.POST['avatar_url']
    s.submission_date = datetime.datetime.now()
    s.save()
    if request.method == 'POST':
        print "post"
        print Submission.objects.all()
    else:
        print "get"
        print Submission.objects.all()
    return render(request, 'submit_forms.html')