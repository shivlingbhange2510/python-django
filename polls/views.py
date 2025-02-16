from django.shortcuts import render
from .models import Question

from django.http import HttpResponse
from django.template import loader

def index2(request):
    return HttpResponse('hello we are inside view.py and inside poll app index fn')
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

    # return ''
def index3(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    response=HttpResponse()
    # HttpResponse.set_cookie(HttpResponse, value='', max_age=None, expires=None, path='/', domain=None, secure=False, httponly=False, samesite=None)
    output = ", ".join([q.question_text for q in latest_question_list])
    data = {"name": 'shivling'}
    # HttpResponse.set_cookie('','testss', value='', max_age=None, expires=None, path='/', domain=None, secure=False, httponly=False, samesite=None)
    response.set_cookie('cookie_name',  value=data)
    response.set_cookie('token',   value='test')
    response.status_code=200
    # response.set_cookie('cookie_name1', value=data)
    # response.set_cookie('cookie_name2', value='test2')

                        # max_age=None, expires=None, path='/', domain=None, secure=False, httponly=False, samesite=None)
    response.write(output)
    return response
# HttpResponse(output)
    
# Create your views here.

def detail(request, question_id):
    lastName='shiv'
    # response=HttpResponse(headers={"Age": 120})
    response=HttpResponse()

    # HttpResponse()
    # response.write('hi this is shiv here') 
    # response = HttpResponse("Here's the text of the web page.")
    response.writelines("You're looking at question %s. username is %s" % (question_id, lastName))
    response.write("<p style='color: red'>Here's the text of the web page.</p>")
    response.write("<p>Here's another paragraph.</p>")
    return response
    # return HttpResponse("You're looking at question %s. username is %s" % (question_id, lastName))



def results(request, question_id):
    print('request', request)
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
