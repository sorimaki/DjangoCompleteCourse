from django.shortcuts import render
from django.http import HttpResponse


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
                <h1>{post['id']} -- {post['title']}</h1>
                <p>{post['description']}</p>
            </div>
'''
    return HttpResponse(html)

def post(request, id):
    print(type(id))
    return HttpResponse(f"{id} ")