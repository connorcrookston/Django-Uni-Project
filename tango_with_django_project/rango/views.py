from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Construct a dictionary to pass to the template engine as its context
    # note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    # return a rendered response to send to the client
    # we make use of the shortcut function to make our lives easier
    # note that the first parameter is the tempate we wish to use
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'name': 'Connor'}
    return render(request, 'rango/about.html', context=context_dict)

