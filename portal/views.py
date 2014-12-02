from django.shortcuts import render
from django.http import HttpResponseRedirect,datetime
from portal.models import SubmissionForm

def uploadSubmission(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            attachment = Submission(attachment = request.FILES['attachment'])
            submission = form.save(commit=False)
            submission.submission_date = datetime.date.today()
            submission.save()
            return HttpResponseRedirect('somewhere with success')
        else:
            form = SubmissionForm()
            
        submissions = Submission.objects.all()
        return render_to_response(
              'portal/work_list.html',
              {'attachments': attachments, 'form': form},
              context_instance=RequestContext(request)
          )