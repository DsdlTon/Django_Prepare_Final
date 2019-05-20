from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'DsdlTon',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 5, 2019'  
    },
    {
        'author': 'Fon',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 25, 2019'  
    },
    
]

abouts = [
    {
        'title': 'About'
    }
]


def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': abouts
    }
    return render(request, 'blog/about.html', context)