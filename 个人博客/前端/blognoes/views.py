from django.shortcuts import render

from blognoes.models import Article


def index(request):
    # 首页
    if request.method == 'GET':
        articles = Article.objects.all()
        return render(request, 'index.html', {'articles': articles})


def info(request, id):
    if request.method == 'GET':
        article = Article.objects.filter(pk=id).first()
        return render(request, 'info.html', {'article': article})



def about(request):
    return render(request, 'about.html')


def fengmian(request):
    return render(request, 'fengmian.html')


def list(request):
    return render(request, 'list.html')

#
# def info(request):
#     # 详情页
#     return render(request, 'info.html')


def time(request):
    return render(request, 'time.html')
