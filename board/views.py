from django.shortcuts import render, redirect
# Create your views here.
def index(request):
    return render(request, "board/index.html")
def about(request):
    return render(request, "board/about.html")
def project(request):
    return render(request, "board/project.html")
def baenaon(request):
    return render(request, "board/baenaon.html")