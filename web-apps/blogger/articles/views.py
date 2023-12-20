from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

def article_list(req):
    articles = Article.objects.all().order_by('date')
    context = {'articles': articles}
    return render(req, 'articles/article_list.html', context)

def article_detail(req, slug):
    # line = ""
    # for article in Article.objects.all():
    #     if article.slug == slug:
    #         return render(req, f"articles/{slug}.html")

    article = Article.objects.get(slug=slug)
    return render(req, "articles/article_detail.html", {'article': article})

@login_required(login_url="/accounts/login/")
def article_create(req):
    if req.method == 'POST':
        form = forms.CreateArticle(req.POST, req.FILES)
        if form.is_valid():
            # save article to DB
            instance = form.save(commit=False)
            instance.author = req.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(req, 'articles/article_create.html', {'form': form})
