from django.shortcuts import render

from articles.models import Article, Scope, ArticleScope


def articles_list(request):
    template = 'articles/news.html'
    oredering = '-published_at'
    articles = Article.objects.order_by(oredering).all()
    context = {'articles': articles}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by

    return render(request, template, context)
