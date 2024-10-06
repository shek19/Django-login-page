from django.http import HttpResponse
import datetime

def index_page(request):
    print("we are in index page")
    return HttpResponse("Welcome to Index Page")

def AboutUS(request):
    print("we are in About US page")
    return HttpResponse("Welcome to About US page")

def dummy(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(f"<center><h1>Hi welcome to <b>DJANGO<b> !  <br> Its a Dummy page <br> {html}</center>")