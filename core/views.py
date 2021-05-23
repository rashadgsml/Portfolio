from django.shortcuts import render, get_object_or_404, redirect
from .models import PortfolioApp, ContactUs

def index(req):
    apps = PortfolioApp.objects.all()
    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        subject = req.POST.get('subject')
        message = req.POST.get('message')
        ContactUs.objects.create(name=name,email=email,subject=subject,message=message)
        return redirect('index')
    return render(req,'index.html',{'apps':apps})

def detail(req, id):
    app = get_object_or_404(PortfolioApp, id=id)
    return render(req,'portfolio-details.html',{'app':app})