from django.shortcuts import render

def index(request):
    return render(request, 'dev4/index.html')