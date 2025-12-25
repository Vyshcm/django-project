from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def print_hello(request):
    movie_data={
        'movies':[
       {
        'title':'God father',
        'year':'1999',
        'author':'padmarajan',
        'success':True
       },
       {
        'title':'goldfish',
        'year':'1990',
        'success':True
       },
       {
        'title':'great father',
        'year':'1999',
        'author':'padmarajan',
        'success':True
       }, 
       {
        'title':'bha ba bha',
        'year':'1999',
        'author':'padmarajan',
        'success':True
        }

    ]}    




    return render(request,'hello.html',movie_data)
  

