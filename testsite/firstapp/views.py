from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


#this basically renders what we need to show 

def index(request):
    return render(request,'index.html')




def counter(request):
    #gets the text object from the reuqest url
    text=request.GET['text']
    amount_of_words=len(text.split())
    return render(request,'counter.html',{'amount':amount_of_words})