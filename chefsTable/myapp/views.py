from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the littlelemon")
    

def hello(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    response = HttpResponse()
    response.headers['Age'] = 20


    msg = f"""
    <br>Path: {path}
    <br>Address: {address}
    <br>Scheme: {scheme}
    <br>Method: {method}
    <br>User agent: {user_agent}
    <br>Path info: {path_info}
    <br>Response_header: {response.headers}

    """
    return HttpResponse(msg, content_type='text/html', charset='utf-8')

def dateTime(request):
    date_time = datetime.today().year
    return HttpResponse(date_time)

def menue(request):
    text = """<h1 style="color:#FACE14">"Welcome to the lemon shop"</h1>"""
    return HttpResponse(text)

def menueItem (request, name):
    items = {
        'apple': 'apple is good for health',
        'orange' : 'orange is also good for health',
        'mocha' : 'type of coffee',
        'tea' : 'type of beverage',
        'lemonade' : 'type of refreshment',
        'pinktea' : 'type of kashmir tea'
    }
    description = items[name]
    return HttpResponse(f'<h2> {name}</h2>' + description )