from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views import View
from django.conf import settings
from django.template import loader
from django.shortcuts import redirect
import json
import collections
from datetime import datetime
from random import randint


class NewsPage(View):
    def get(self, request, *args, **kwargs):
        with open('./hypernews/news.json') as json_file:
            news_dict = json.load(json_file)
        context = {}

        q = request.GET.get('q')
        news_dict_q = []
        if q:

            for new in news_dict:
                if str(q) in new["title"]:
                    news_dict_q.append(new)

            for new in news_dict_q:
                date = new["created"].split()[0]
                if date not in context:
                    context[date] = [new]
                else:
                    context[date].append(new)

        else:

            for new in news_dict:
                date = new["created"].split()[0]
                if date not in context:
                    context[date] = [new]
                else:
                    context[date].append(new)

        template = loader.get_template('news.html')
        context = {'context': collections.OrderedDict(sorted(context.items(), reverse=True))}
        return HttpResponse(template.render(context, request))


class NewsView(View):
    def get(self, request, news_link, *args, **kwargs):
        with open('./hypernews/news.json') as json_file:
            news_dict = json.load(json_file)
        new_to_return = None

        for new in news_dict:
            if str(new["link"]) == news_link:
                new_to_return = new
                break

        template = loader.get_template('new.html')
        context = {'news': new_to_return}
        return HttpResponse(template.render(context, request))


class NewsCreate(View):
    def get(self, request, *args, **kwargs):
        template = loader.get_template('create_new.html')
        context = {}
        return HttpResponse(template.render(context, request))

    def post(self, request, *args, **kwargs):
        with open('./hypernews/news.json') as json_file:
            news_dict = json.load(json_file)

        title = request.POST.get('title')
        text = request.POST.get('text')
        created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        link = int(datetime.now().timestamp())
        post_new = {"created": created, "text": text, "title": title, "link": link}
        news_dict.append(post_new)
        with open('./hypernews/news.json', 'w') as json_file:
            json_file.write(json.dumps(news_dict))

        return redirect('/news/')
