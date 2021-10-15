from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, If you see me all works I changed!")
