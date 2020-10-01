from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from home.models import Contact, Counselling, faq

# Create your views here.
def home(request):
    allqna = faq.objects.all()
    questionss = {'allqna' : allqna}
    return render(request, 'home/home.html', questionss)
    # return HttpResponse('This is home page')

def materials(request):
    return render(request, 'home/materials.html')
    # return HttpResponse("This is paterials page")

def buy_course(request):
    return render(request, 'home/buy_course.html')
    # return HttpResponse("This is buy a course page")

def counselling(request):
    if request.method == 'POST':
        fname1 = request.POST['fname1']
        lname1 = request.POST['lname1']
        email1 = request.POST['email1']
        phone1 = request.POST['phone1']
        content1 = request.POST['content1']
        modes = request.POST['modes']

        if len(fname1)<2 or len(lname1)<2 or len(email1)<5 or len(phone1)<10 or len(content1)<15:
            messages.error(request, 'Please fill the form correctly')

        else:
            ss1 = Counselling(fname1=fname1, lname1=lname1, email1=email1, phone1=phone1, content1=content1, modes=modes)
            ss1.save()

            messages.success(request, 'Your response has been submited')

    return render(request, 'home/counseeling.html')
    # return HttpResponse("this is counselling page")

def about_us(request):
    return render(request, 'home/about.html')
    # return HttpResponse("This is about us page")

def contact(request):
    # this is store data in database and valodate the form
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(fname)<2 or len(lname)<2 or len(email)<5 or len(phone)<10 or len(content)<15:
            messages.error(request, 'Please fill the form correctly')

        else:
            ss = Contact(fname=fname, lname=lname, email=email, phone=phone, content=content)
            ss.save()

            messages.success(request, 'Your response has been submited')
    return render(request, 'home/contact.html')
    # return HttpResponse("This is about us page sasa")