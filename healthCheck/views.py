from django.shortcuts import render

# Create your views here.

def healthCheck(request):

    return render(request,'healthCheck/healthCheck.html')
