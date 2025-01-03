from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
#from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Post
from django.shortcuts import get_object_or_404 

"""
posts = [
    {
        'id':1,
        'title': 'Title 1',
        'description': 'Title 1 Description',
    },
    {
        'id':2,
        'title': 'Title 2',
        'description': 'Title 2 Description',
    },
    {
        'id':3,
        'title': 'Title 3',
        'description': 'Title 3 Description',
    },
]
"""
#Sposts = []

# Create your views here.
"""
def home(request): 
Old home code 
    html = ""

    for post in posts:
        html +=  f'''
            <div>
                <a href="/post/{post['id']}/"
                <h1>{post['id']} -- {post['title']}</h1></a>
                <p>{post['description']}</p>
            </div>
'''
    return render(request, 'posts/index.html', {'name':'BUBU', 'list':posts} ) 
def post(request, id):
Old post code
    #print(type(id))
    valid_id = False
    for post in posts:
        if post['id']==id:
            post_dict = post
            valid_id = True
            break

    if valid_id == True:
        html = f'''
                <div>
                    <h1>{post_dict['id']} -- {post_dict['title']}</h1>
                    <p>{post_dict['description']}</p>
                </div>
        '''
        
        return render(request, 'posts/post.html', {'post_dict':post_dict})
    else:
        # return HttpResponseNotFound("These are not the droids you are looking for")
        raise Http404()    
"""

def home(request):
    all_posts = Post.objects.all()
    #print(all_posts)
    return render(request, 'posts/index.html', {'name':'BUBU', 'list':all_posts} ) 

def post(request, id):
    """try:
        post = Post.objects.get(id=id)
    except:
        raise Http404()"""
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/post.html', {'post_dict':post})

def google(request, id):
    url = reverse('post', args=[id])
    #return HttpResponseRedirect(f'/post/{id}') 
    return HttpResponseRedirect(url) 

def global1(request):
    return render(request, 'global.html')