from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from datetime import datetime
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def add_money(request):
    if request.method == "POST" or request.method == "GET":
        if 'activities' not in request.session:
            request.session['activities'] = []
        
        if 'count' not in request.session:
            request.session['count'] = 0
        
        if 'farm' in request.POST:
            golds = random.randrange(10,20)
            request.session['count'] += golds
            Gold_earned = {
                "name":'farm', 
                "amount": golds,
                "timestamp": str(datetime.now()),
                "result" : 'win'
            }
            request.session['activities'].append(Gold_earned)
            request.session.modified= True
            
        if 'cave' in request.POST:
            golds = random.randrange(5,10)
            request.session['count'] += golds
            Gold_earned = {
                "name":'cave', 
                "amount": golds,
                "timestamp": str(datetime.now()),
                "result" : 'win'
            }
            request.session['activities'].append(Gold_earned)
            request.session.modified= True
            
        if 'house' in request.POST:
            golds = random.randrange(2,5)
            request.session['count'] += golds
            Gold_earned = {
                "name":'house', 
                "amount": golds,
                "timestamp": str(datetime.now()),
                "result" : 'win'
            }
            request.session['activities'].append(Gold_earned)
            request.session.modified= True
            
        if 'casino' in request.POST:
            golds = random.randrange(-50,50)
            request.session['count'] += golds
            Gold_earned = {
                "name":'casino', 
                "amount": golds,
                "timestamp": str(datetime.now()),
                "result" : 'win' if golds >= 0 else 'lost'
            }
            request.session['activities'].append(Gold_earned)
            request.session.modified= True
            
        # print('helloo',request.POST)
    return redirect('/')
def reset(request):
    if 'count' in request.session:
        del request.session['count']
    if 'activities' in request.session:
        del request.session['activities']
    return redirect('/')