from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import sys, os
sys.path.insert(1, os.path.dirname(os.path.abspath(__file__)))
from summerizeTest import *

def index(request):
    return  HttpResponse(SummerizeTest())
    # return HttpResponse(os.path.dirname(os.path.abspath(__file__)))