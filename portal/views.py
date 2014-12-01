from django.shortcuts import render
from django.http import HttpResponseRedirect
from portal.models import SubmissionForm

def uploadSubmission(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.submission_date = datetime.date.today()
            submission.save()
            return HttpResponseRedirect('/success')
            
        return render(request, '/form_upload.html', {
                'form': form,
            })