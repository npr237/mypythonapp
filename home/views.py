from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    messages.success(request,"This is a success")
    context={
        'variable1':"this is harry",
        'variable2':"this is cherry",
        'variable3':"this is karry"
    }
    return render(request,'index.html',context)

    
   # return HttpResponse('this is homepage')
def about(request):
     return render(request,'about.html')
   # return HttpResponse('this is aboutpage')
def services(request):
      return render(request,'services.html')
   # return HttpResponse("this is services")
def contact(request):
      if request.method == "POST":
           name=request.POST.get('name')
           phone=request.POST.get('phone')
           email=request.POST.get('email')
           password=request.POST.get('password')
           desc=request.POST.get('desc')
           contact=Contact(name=name,phone=phone,email=email,password=password,desc=desc,date=datetime.today())
           contact.save()
           messages.success(request, "Your data has been saved!.")
           
      return render(request,'contact.html')
   # return HttpResponse("this is contact")

#url dispatching samajh aa gya ab templates samajhna h chizn ko khubsurat bnao

    

    
