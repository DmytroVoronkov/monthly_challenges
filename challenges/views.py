from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

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
    'dcember': 'Numquam molestiae sed.'
}


# Create your views here.
def monthly_challenge(request, month: str):
    if month not in monthly_challenges.keys():
        return HttpResponseNotFound("Invalid month")
    
    challenge_text = monthly_challenges[month]
    return HttpResponse(challenge_text)