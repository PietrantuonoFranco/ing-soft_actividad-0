from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Question

#__________INDEX_____________________________________________________
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    
    context = {
        "latest_question_list": latest_question_list
    }

    return render(request, "polls/index.html", context)



#__________DETAIL_____________________________________________________
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls/detail.html", { "question": question })



#__________RESULTS_____________________________________________________
def results(request, question_id):
    response = "You're looking at the results of question %s."
    
    return HttpResponse(response % question_id)




#_________VOTE_____________________________________________________
def vote(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)