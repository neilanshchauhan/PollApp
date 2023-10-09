from django.shortcuts import render
from .models import Question,Choices

# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('-published')[:5]
    context = {'latest_questions':latest_questions}
    return render(request,'polls/index.html',context)