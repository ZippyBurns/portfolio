from django.shortcuts import render, redirect, HttpResponse

def index(request):
    if request.method == "GET":
        return render (request, 'index.html')