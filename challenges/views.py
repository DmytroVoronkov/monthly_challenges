from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string


monthly_challenges = {    
    'january': 'Corporis cupiditate fugit deserunt repellendus.',
    'february': 'Accusamus hic dolor.',
    'march': 'Aut et voluptate voluptatum ab sed magni quos.',
    'april': 'Dolor maxime cupiditate occaecati qui.',
    'may': 'Nobis iure est odio.',
    'june': 'Eum qui facere autem.',
    'july': 'Eum atque earum error autem harum cum est et autem.',
    'august': 'Repudiandae ea unde odio porro velit ipsum atque.',
    'september': 'Rem reprehenderit adipisci doloremque est quibusdam repellat iure.',
    'october': 'Reprehenderit totam sunt quam inventore ut minima aut.',
    'november': 'Et dignissimos velit ipsum quia.',
    'december': 'Numquam molestiae sed.'
}


# Create your views here.
def index(request):
    response_data = 'None'
    for month in monthly_challenges.keys():
        response_data += f"<li><a href='{reverse('month-challenge', args=[month])}'>{month.capitalize()}<a/></li>"
        
    response_data = f"<ul>{response_data}</ul>"
    return HttpResponse(response_data)

def monthly_challenge(request, month: str):
    try:
        # challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html')
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound('No month found')
    
    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)