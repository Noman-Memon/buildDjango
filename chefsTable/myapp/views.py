from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from myapp.forms import InputForm, BookingForm, Booking

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

def menu(request):
    text = """<h1 style="color:#FACE14">"Welcome to the lemon shop"</h1>"""
    newmenu = {'mains':[
        {'name':'falfel', 'price':'12'},
        {'name':'orange juice', 'price':'25'},
        {'name':'apple juice', 'price':'50'},
    ]}

    return render(request, 'menu.html', newmenu)

def about(request):
    about_content = {'about':"Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."}
    return render(request, 'about.html', about_content)

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


def form(request):
    form = InputForm()
    context = {"form":form}
    return render(request, "home.html", context)
    
def form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "home.html", context)

def my_bookings(request):
    my_bookings = Booking.objects.all()
    my_booking_dic = {'bookings' : my_bookings}
    return render(request, 'my_bookings.html', my_booking_dic)