from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from blogb.settings import ORDER_NUMBER
from blogback.forms import RegisterForm, LoginForm, CategoryForm, ArticleForm
from blogback.models import User, Category, Article


def index(request):
    """主页"""
    return render(request, 'index.html')


def add_flink(request):
    """增加友情链接"""
    return render(request, 'add-flink.html')


def add_notice(request):
    """撰写新公告"""
    return render(request, 'add-notice.html')


def comment(request):
    """评论栏"""
    return render(request, 'comment.html')


def flink(request):
    """友情链接等其他操作"""
    return render(request, 'flink.html')


def loginlog(request):
    """用户登陆使用记录"""
    return render(request, 'loginlog.html')


def manage_user(request):
    """用户管理"""
    return render(request, 'manage-user.html')


def notice(request):
    """公告操作"""
    return render(request, 'notice.html')


def readset(request):
    """用户设置"""
    return render(request, 'readset.html')


def setting(request):
    """常规设置"""
    return render(request, 'setting.html')


def update_flink(request):
    """修改友情链接"""
    return render(request, 'update-flink.html')


def register(request):
    """用户注册"""
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = make_password(form.cleaned_data['userpwd'])
            User.objects.create(username=username, password=password)
            return HttpResponseRedirect(reverse('blogback:login'))
        else:
            errors = form.errors
            return render(request, 'register.html', {'errors': errors})


def login(request):
    # 用户登录
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = User.objects.filter(username=username).first()
            request.session['user_id'] = user.id
            return HttpResponseRedirect(reverse('blogback:index'))
        else:
            errors = form.errors
            return render(request, 'login.html', {'errors': errors})


def logout(request):
    # 退出登录
    if request.method == 'GET':
        del request.session['user_id']
    return HttpResponseRedirect(reverse('blogback:login'))


def add_category(request):
    """增加栏目"""
    if request.method == 'GET':
        categorys = Category.objects.all()
        return render(request, 'category.html', {'categorys': categorys})

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            alias = form.cleaned_data['alias']
            keywords = form.cleaned_data['keywords']
            describe = form.cleaned_data['describe']
            fid = form.cleaned_data['fid']
            Category.objects.create(cate_name=name,
                                    cate_alias=alias,
                                    cate_keywords=keywords,
                                    cate_describe=describe,
                                    cate_fid_id=fid)
            return HttpResponseRedirect(reverse('blogback:add_category'))
        else:
            errors = form.errors
            return render(request, 'category.html', {'errors': errors})


def update_category(request, id):
    """修改栏目表"""
    if request.method == 'GET':
        categorys = Category.objects.all()
        set_category = Category.objects.filter(pk=id).first()
        return render(request, 'update-category.html', {'set_category': set_category, 'categorys': categorys})

    if request.method == 'POST':
        category = CategoryForm(request.POST)
        if category.is_valid():
            cate_name = category.cleaned_data['name']
            cate_alias = category.cleaned_data['alias']
            cate_keywords = category.cleaned_data['keywords']
            cate_describe = category.cleaned_data['describe']
            cate_fid_id = category.cleaned_data['fid']
            Category.objects.filter(pk=id).update(cate_name=cate_name,
                                                  cate_alias=cate_alias,
                                                  cate_keywords=cate_keywords,
                                                  cate_describe=cate_describe,
                                                  cate_fid_id=cate_fid_id)
            return HttpResponseRedirect(reverse('blogback:category'))
        else:
            errors = category.errors
            return render(request, 'update-category.html', {'errors': errors})


def del_category(request, id):
    if request.method == 'GET':
        Category.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('blogback:category'))


def add_article(request):
    """添加文章"""
    if request.method == 'GET':
        categorys = Category.objects.all()
        return render(request, 'add-article.html', {'categorys': categorys})

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            keywords = form.cleaned_data['keywords']
            describe = form.cleaned_data['describe']
            category = request.POST.get('category')
            Article.objects.create(art_title=title,
                                   art_content=content,
                                   art_keywords=keywords,
                                   art_describe=describe,
                                   art_cid_id=category)
            return HttpResponseRedirect(reverse('blogback:article'))
        else:
            errors = form.errors
            return render(request, 'add-article.html', {'errors': errors})


def article(request):
    """文章管理"""
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        articles = Article.objects.all()
        arttests = []
        for article in articles:
            cid = article.art_cid_id
            ca_name = Category.objects.get(pk=cid).cate_name
            arttest = [article, ca_name]
            arttests.append(arttest)
        pg = Paginator(arttests, ORDER_NUMBER)
        arttests = pg.page(page)
    return render(request, 'article.html', {'arttests': arttests})


def update_article(request, id):
    """文章修改"""
    if request.method == 'GET':
        set_article = Article.objects.filter(pk=id).first()
        categorys = Category.objects.all()
        return render(request, 'update-article.html', {'set_article': set_article, 'categorys': categorys})

    if request.method == 'POST':
        article = ArticleForm(request.POST)
        if article.is_valid():
            art_title = article.cleaned_data['title']
            art_content = article.cleaned_data['content']
            art_keywords = article.cleaned_data['keywords']
            art_describe = article.cleaned_data['describe']
            art_cid_id = article.cleaned_data['category']
            Article.objects.filter(pk=id).update(art_title=art_title,
                                                 art_content=art_content,
                                                 art_keywords=art_keywords,
                                                 art_describe=art_describe,
                                                 art_cid_id=art_cid_id
                                                 )
            return HttpResponseRedirect(reverse('blogback:article'))
        else:
            errors = article.errors
            return render(request, 'update-article.html', {'errors': errors})


def del_article(request, id):
    if request.method == 'GET':
        Article.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('blogback:article'))
