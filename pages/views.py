from django.shortcuts import render
from django.http import HttpResponse

def landingPageView(request):
    return render(request, 'pages/landingPage.html')

def importPageView(request):
    return render(request, 'pages/importPage.html')