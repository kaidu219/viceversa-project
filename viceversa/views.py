from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def reverse(request):
    user_text = request.GET['usertext']
    reversed_test = user_text[::-1]
    s = user_text.split()
    l = len(s)
    return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext':reversed_test, 'count_words':l})


