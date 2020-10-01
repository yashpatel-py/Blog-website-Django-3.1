from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from django.contrib import messages

# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.html', context)

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()

    post.views = post.views + 1
    post.save()

    context = {'post':post}
    return render(request, 'blog/blogPost.html', context)

def search(request):
    result = request.GET['result']

    if len(result) > 50:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains = result)
        allPostsContent = Post.objects.filter(disp__icontains = result)
        allPostsCat = Post.objects.filter(cat__icontains = result)

        allPosts = allPostsTitle.union(allPostsContent, allPostsCat)
    
    if allPosts.count() == 0:
        messages.warning(request, 'Please fill the form correctly')

    params = {'allPosts' : allPosts, 'result' : result}
    return render(request, 'blog/search.html', params)