from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

# methods


def root(request):
    return redirect('/blogs')


def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")


def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")


def create(request):
    return redirect('/')


def show(request):
    return HttpResponse("placeholder to display blog number: {number}")


def edit(request):
    return HttpResponse("placeholder to edit blog {number}")


def destroy(request):
    return redirect('/blogs')


def json(request):
    return JsonResponse({'title': 'First Blog', 'content': 'Some content'})
