from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator , EmptyPage ,PageNotAnInteger
import io
import json
import requests
# Create your views here.



def get_question(request):
    if request.method == 'POST':
        language = request.POST['language']
        print(language)
        url = 'https://api.stackexchange.com/questions?site=stackoverflow&tagged='
        resp = requests.get(url + language)
        print(resp.url)
        questions_list = resp.json()
        print(type(resp))
        print(type(questions_list))


        questions = []

        for quest in questions_list['items']:
            q = (quest['tags'],quest['title'],quest['answer_count'])
            questions.append(q)
        print(len(questions))

        #pagination
        paginator = Paginator(questions,10)
        page = request.GET.get('page')
        pagi = paginator.get_page(page)
        print(pagi)
        print(page)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
    else:
        questions = {}
        posts = {}
        page = 0

    return render(request,'questions/myquestion.html',{'questions':posts,'page':page})
