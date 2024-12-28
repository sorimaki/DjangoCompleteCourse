from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


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

# Create your views here.
def home(request):
    html = ""

    for post in posts:
        html +=  f'''
            <div>
                <a href="/post/{post['id']}/"
                <h1>{post['id']} -- {post['title']}</h1></a>
                <p>{post['description']}</p>
            </div>
'''
    return HttpResponse(html) 

def post(request, id):
    
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
        
        return HttpResponse(html)
    else:
        return HttpResponseNotFound("These are not the droids you are looking for")

def google(request):
    return HttpResponseRedirect('https://www.google.com') 