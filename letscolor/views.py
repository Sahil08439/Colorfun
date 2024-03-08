from django.shortcuts import render
from .models import contact_info

# Create your views here.
def home(request):
    return render(request, 'letscolor/home.html')

def coloring(request):
    return render(request, 'letscolor/coloring.html')

def Contact(request):
    # return HttpResponse('<h1>This is My Contact Page </h1>')
   if request.method == 'GET':
        return render(request, 'letscolor/contact.html')
   elif request.method == 'POST':
        email = request.POST.get('user_email')
        message = request.POST.get('message')
        x = contact_info(u_email=email, u_message=message)
        x.save()
        print(email)
        print(message)
        return render(request,"letscolor/contact.html",{'feedback':'Your message has been recorded'})