from django.shortcuts import render
import socket

# Create your views here.
def main(request):
    #ip = socket.gethostbyname(socket.gethostname())



    return render(request, 'index.html')