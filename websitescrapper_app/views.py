import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render
from bs4 import BeautifulSoup
from .models import Links
# Create your views here.
def home(request):
    if request.method =='POST':
        link_new=request.POST.get('page','')
        urls=requests.get(link_new)
        beautysoup=BeautifulSoup(urls.text,'html.parser')
        for link in beautysoup.find_all('a'):
            address=link.get('href')
            name=link.string
            Links.objects.create(address=address,stringname=name)
        return HttpResponseRedirect('/')
    else:
        data_values=Links.objects.all()
        #print(address)
    return render(request,'home.html',{'datavalues':data_values})
