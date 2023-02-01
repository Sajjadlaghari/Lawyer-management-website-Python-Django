from django.http import HttpResponse
from django.shortcuts import render


def aboutUs(request):
    return render(request,'about.html')

def contactUs(request):
    return render(request,'contact.html')

def whoAreWe(request):
    return HttpResponse("Welcome to the Who are we Page")

def detailed(request,id):
    return HttpResponse("Detailed of Page with Id Number is " + id)

def homePage(request):
    # data ={
    #     'title':"Home Page",
    #     'lang':["Python","Java","PHP","R"],
    #     'students':[
    #         {'name':'Sajjad Ali','email':'sajjad@gmail.com','phone':'03003929585','address':"Village "},
    #         {'name':'Ali','email':'ali@gmail.com','phone':'03003929585','address':"City "},
    #         {'name':'Test','email':'test@gmail.com','phone':'02443422','address':"Village "},
    #         {'name':'Test1','email':'test1@gmail.com','phone':'03243442324','address':"Village and City "},
    #         {'name':'Test2','email':'test2@gmail.com','phone':'03242345522','address':"Both "},
    #     ]
    # }
    return render(request,'index.html')

def cal(request):
    return render(request,'cal.html')


def sum(request):
    try:
          val1 = int(request.POST['val1'])
          val2 = int(request.POST['val2'])
          res = val1+val2
          print(res)
          return render(request,'cal.html',{'output':res})
    except:
          return render(request,'cal.html')


    # return render(request,'cal.html')
