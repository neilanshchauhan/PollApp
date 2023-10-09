from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Question,Choices

# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('-published')[:5]
    context = {'latest_questions':latest_questions}
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    
    return render(request,'polls/results.html',{'question':question})

def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})