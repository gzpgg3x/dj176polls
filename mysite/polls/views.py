from django.shortcuts import render
from django.http import HttpResponse
# from django.template import ContextResponse, loader
from django.template import RequestContext, loader
from polls.models import Question, Choice
from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


# def index(request):
#     return HttpResponse('Hello World, this is polls homepage.')

##per djangoproject tutorial
# def index(request):    
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([p.question_text for p in latest_question_list])
#     return HttpResponse(output) 

# # by following tangowithdjangno (works will)
# def index(request):
#     context = RequestContext(request)
#     latest_question_list = Question.objects.order_by('-pub_date')[:2]
#     context_dict = {'latest_question_list': latest_question_list}
#     return render_to_response('polls/index.html', context_dict, context) 

# # Per djangoproject tutorial
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:2]
#     template = loader.get_template('polls/index.html')
#     context = RequestContext(request, {'latest_question_list': latest_question_list,})    
#     return HttpResponse(template.render(context))

# Per djangoproject tutorial shortcuts
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:2]
    context = {'latest_question_list': latest_question_list,}
    return render(request, 'polls/index.html', context)    

# # Per djangoproject tutorial
# def detail(request, question_id):
#     return HttpResponse('You are looking at question %s.' % question_id)

# # before A shortcut: get_object_or_404()
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404('Question does not exist')
#     return render(request, 'polls/detail.html', {'question': question})

# A shortcut: get_object_or_404()
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

# # Placeholder prior Tutorial 4
# def results(request, question_id):
#     response = "You are look at the results of question %s."
#     return HttpResponse(response % question_id)

# # djangoproject's dummy version
# def vote(request, question_id):
#     response = "Vote here for question %s."
#     return HttpResponse(response % question_id)

def vote(request, question_id):
    # p = get_object_or_404(Question, id=question_id)
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voiting form.
        return render(request, 'polls/detail.html', {'question': p, 'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing 
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})



