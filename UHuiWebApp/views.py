from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'U.html', {
            'question': "a",
            'error_message': "You didn't select a choice.",
        })