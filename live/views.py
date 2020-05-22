from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
import datetime
# Create your views here.
def index(request):
      url = "https://covid-193.p.rapidapi.com/statistics"
      querystring={"country":"India"}
      headers = {'x-rapidapi-host': "covid-193.p.rapidapi.com",'x-rapidapi-key': "da8787ce4bmsh535295cb53bc7aap1c15a1jsn435a4f72ab66"}
      response = requests.request("GET", url, headers=headers,params=querystring).json()

      
      data=response['response']
      d=data[0]

      
      
    #   print(d)
      context={
          "developer":"Er. Saurabh Tripathi",
          "LastUpdate":d['day'] ,
          'totalinf':d['cases']['total'],
          "activecase":d['cases']['active'],
          "newcases":d['cases']['new'],
          "Recovered":d['cases']['recovered'],
          "critical":d['cases']['critical'],
          "totdeaths":d['deaths']['total'],
          "newdeaths":d['deaths']['new'],
          "tottests":d['tests']['total'],
          "time":d['time']

      }
      return render(request,'index.html',context)
