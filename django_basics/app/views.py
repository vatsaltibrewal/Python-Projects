from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    '''
    Main Index View
    
    :param request: Basic HTTP request object
    :return: HttpResponse with a welcome message
    '''
    return render(request, 'index.html')