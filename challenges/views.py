from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def index(request):
    return HttpResponse("Hello Django!")

def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "Run every day"
    else:
        return HttpResponseNotFound("No challenge this month")
    return HttpResponse(challenge_text)