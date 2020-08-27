from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.core.mail import send_mail
from . models import Visitor,BannedIP,UntrackedUserAgent

# Create your views here.
def page_views(request,post_id):
    page_object = Visitor.objects.get(id=post_id)
    page_object.page_visits += 1
    page_object.save()

def home(request):
    return render(request,'dashapp/index.html')

def send_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        send_mail('Subject goes here',
        'Message goes here',
        'noreply@authapplication.com',[email],
        fail_silently=False)
        return HttpResponse(' Mail Sent To ' + email)

    return render(request,'dashapp/send_email.html')        

    