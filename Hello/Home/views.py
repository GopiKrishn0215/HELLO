from django.shortcuts import render, HttpResponse

# Create your views here.
def ind(request):
    context={
        'variable':"This is sent"
    }
    return render(request,'index.html',context)

def about(request):
    return HttpResponse("This is about page")

def services(request):
    return HttpResponse("This is service page")