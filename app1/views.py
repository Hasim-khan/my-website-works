from django.shortcuts import render,redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.views import View
from .models import *
from django.urls import reverse
import sweetify

from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import get_object_or_404, redirect
# Create your views here.
# class home(View):
#     def get(self,request):
#         return HttpResponse("hello dabbu") -blog
    
def index(request):
    return render(request,"index.html")

def faqs(request):
    return render(request,"faqs.html")



def about_us(request):
    return render(request,"About.html")

def Contact(request):
    return render(request,"contact.html")

def services(request):
    return render(request, 'services.html')

def servicedetails(request):
    return render(request, 'service-details.html')

def teamdetails(request):
    return render(request, 'team-details.html')

def pricingplans(request):
    return render(request, 'pricing-plans.html')

## projects cms creation .reverse()
class ourprojects(View):
    def get(self,request):
        data = project_cms.objects.all().order_by('id') 
        return render(request, 'our-projects.html', {'cmsdata': data})
class projectdetails(View):
    def get(self, request, slug):
        project_data = project_cms.objects.get(project_title=slug)
        return render(request, 'project-details-2.html',{'project_data': project_data})

class ourblog(View):
    def get(self, request):
        blog_data = blog_cms.objects.all().order_by('id')
        return render(request,"our-blog.html", {'blog_data' : blog_data})

def blogdetails(request):
    return render(request,"blog-details.html")


def contactform(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        message = request.POST.get('message')
        data = ContactData.objects.create(name=name, email=email, message=message, contact=contact)
        data.save()
        ### send thankyou mail ###
        subject = "Thankyou For Contacting Us"
        email_html = render_to_string("Thankyoumail/email.html", {'name': name})
        email_text = strip_tags(email_html)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, email_text, from_email, [email], html_message=email_html)

        sweetify.success(request, 'Hey!!!', text = 'We Will Contact You Soon!', persistent = 'Done')
        return redirect('contactform')
    return render(request, 'contact.html')



### its login method of user
def loginpage(request):
    return render(request,"login/loginpage.html")

def adminform(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')  # Corrected typo in password field
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/userhome')
        else:
            # Pass error message to template
            return render(request, "login/loginpage.html", {"error_message": "Sorry, wrong password!"})
    return render(request, "login/loginpage.html")
def userhome(request):
    return render(request,"login/userhome.html")

def forgetpasspage(request):
    return render(request,"forgotpassword/forgetpass.html")


def userlogout(request):
    logout(request)
    return redirect(index)


def allrecord(request):
    alldata = ContactData.objects.all
    return render(request,"login/allrecords.html", {'alldata':alldata})

def delete_record(request, record_id):
    record = get_object_or_404(ContactData, id=record_id)
    record.delete()
    sweetify.success(request, 'Hey!!!', text = 'Successfully Deleted!!!', persistent = 'Done')

    return redirect('allrecord') 



## this is simple way
# def delete_record(request):
#     if request.method=="DELETE":
#         name=request.POST.get("name")
#         r=ContactData.objects.filter(name=name)
#         r.delete()
#     return render(request,"delete.html",{'msg':"successfully deleted"})


## its simple mail procedure
        # subject = "Thankyou For Contacting Us"
        # message_body = f"Dear {name},\n\nThank you for reaching out to us. We will get back to you soon.\n\nBest regards,\nYour Company"
        # from_email = settings.EMAIL_HOST_USER
        # send_mail(subject, message_body, from_email, [email])  

