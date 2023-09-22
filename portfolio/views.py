from django.shortcuts import render
from .models import Project, Contact
from django.contrib import messages

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})


def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        content=request.POST['content']
        print(name, email, content)

        if len(name)<2 or len(email)<2 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:    
          contact = Contact(name=name, email=email, content=content)
          contact.save()
          messages.success(request, "Your message has been sent")
    return  render(request, 'portfolio/contact.html')