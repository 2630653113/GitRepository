from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_view(request):
    return HttpResponse('Let\'t finish this Web together!')
