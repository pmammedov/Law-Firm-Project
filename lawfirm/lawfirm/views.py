from django.http import HttpResponse

def homepage(request):
    return HttpResponse('Lets say bismillah!')

def about(request):
    return HttpResponse('This is about!')