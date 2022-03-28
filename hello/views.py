from django.shortcuts import render
from hello.models import Reports
from hello.models import temp_measure
from hello.models import heart_measure
from django.contrib import messages
import requests
import joblib
import random
# Create your views here.
def hello(request):
    return render(request,'hello.html')
    
def about(request):
    #return HttpResponse("This is about Homepage")
    return render(request,'about.html')
def contact(request):
    if request.method=='POST':
        query=request.POST['query']
        Reports(query=query).save()
        messages.success(request,"Your query has been received")
        return render(request,'contact.html')
    else:
        return render(request,'contact.html')
    

def services(request):
    #return HttpResponse("This is services Homepage")
    return render(request,'services.html')


def appointment(request):
    
    if request.method=="POST":
        email=request.POST['email']
        pwd=request.POST['pwd']
        age=request.POST['age']
        disease=request.POST['disease']
        ailments=request.POST['ailments']
        #Userdetails=User.objects.get(disease=request.POST['disease'],ailments=request.POST['ailments'])
        model=joblib.load('ml_model1.sav')
        lis=[]
        
        lis.append(request.POST.get('age'))
        lis.append(request.POST.get('disease'))
    
        lis.append(request.POST.get('ailments'))
        ans=model.predict([lis])
        return render(request, 'appointment.html',{'ans':ans})
    else:
        return render(request,'appointment.html')





def result(request):
    return render(request,'result.html')

def helpline(request):
    return render(request,'helpline.html')

def login(request):
    if request.method=="POST":
        try:
            Userdetails=Reports.objects.get(email=request.POST['email'],pwd=request.POST['pwd'])
            print("Username=",Userdetails)
            request.session['email']=Userdetails.email
            messages.success(request,'Success!! Logged in!')
            return render(request,'hello.html')
        except Reports.DoesNotExist as e:
            messages.success(request,"Username / Password is Invalid")
    return render(request,'login.html')
    
def logout(request):
    try:
        del request.session['email']
    except:
        return render(request,'hello.html')
    return render(request,'hello.html')

def signup(request):
    if request.method=="POST":
        pname=request.POST['pname']
        email=request.POST['email']
        mobileno=request.POST['mobileno']
        bloodgroup=request.POST['bloodgroup']
        locationinfo=request.POST['locationinfo']
        pwd=request.POST['pwd']
        disease=request.POST['disease']
        ailments=request.POST['ailments']
        age=request.POST['age']
        Reports(pname=pname, email=email, mobileno=mobileno, bloodgroup=bloodgroup, locationinfo=locationinfo, pwd=pwd, disease=disease, ailments=ailments, age=age).save()
        messages.success(request, 'The New user'+request.POST['pname']+'Is saved Successfully..!')
        return render(request,'signup.html')
    else:
        return render(request,'signup.html')
   
def notification(request):

    num = random.randint(1,32)

    temp = temp_measure.objects.get(pk=num)
    heart = heart_measure.objects.get(pk=num)


    return render(request,'notification.html',{'temp':temp,'heart':heart})



def register(request):
    #return HttpResponse("This is services Homepage")
    return render(request,'signup.html')
# Create your views here.
