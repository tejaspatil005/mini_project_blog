from django.shortcuts import render
from django.http import HttpResponse

post=[
    {
        'author':'Tejas patil',
        'title':'Blog Post 1',
        'content':'first post content',
        'date_posted':'August 1, 2025'
    },
    {
        'author':'riya patil',
        'title':'blog post 2',
        'content':'second post content',
        'date_posted':'oct 2 ,2025'
    }
]
def home(request):
    context={
        'posts':post
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'about'})
