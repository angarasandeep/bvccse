from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    o = Year.objects.all()
    return render(request,'bvce/index.html',{"year" : o})

def textbook(request,id):
    # return HttpResponse(id)
    o = Textbook.objects.filter(year=id)
    return render(request,'bvce/textbook.html',{"textbooks":o})

def syllab(request, id):
    o = Syllabus.objects.filter(year=id)
    return render(request, 'bvce/syllabus.html', {"syllab": o})