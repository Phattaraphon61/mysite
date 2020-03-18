from django.shortcuts import render
from .models import problem , problem_select
from datetime import date

# Create your views here.
def mainpage(req):
    data = problem.objects.all()
    return render(req,'index.html',{'datas': data})

def selectdata(req):
    data = req.POST
    for i in data :
        if (i != "csrfmiddlewaretoken"):
            problem_select.objects.create(
            problem_name = i,
            username_select = "amd",
            problem_date_select = date.today())
        

    

