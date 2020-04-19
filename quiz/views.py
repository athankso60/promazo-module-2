from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template import loader
from django.contrib.auth.decorators import login_required


# Create your views here.
from django.http import HttpResponse

from .models import Quiz
from .models import Question

@login_required
def index(request): #quizzes will show up here
    quiz_list = Quiz.objects.all()
    template = loader.get_template('quiz/index.html')
    context = {
        'quiz_list':quiz_list,
    }
    return HttpResponse(template.render(context, request))

@login_required
def detail(request, quiz_id):
    currentQuiz = get_object_or_404(Quiz, pk=quiz_id)
    question_list = get_list_or_404(Question, quiz_foreign_key = quiz_id)
    context = {
        'currentQuiz': currentQuiz,
        'question_list': question_list
    }
    return render(request, 'quiz/detail.html', context)


    
