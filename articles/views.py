from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
# Create your views here.

def article_detail_view(request,id=None):
    article_object = None
    if id is not None:
        article_object = Article.objects.get(id=id)
    context = {
        "article_object":article_object
    }
    return render(request,'detail.html',context)

def article_search_view(request):
    query_dict = request.GET.get('q')
    try:
        query_dict = int(query_dict)
    except:
        query_dict = None
    article_object = None
    if query_dict is not None:
        article_object = Article.objects.get(id=query_dict)
    context = {'article_object': article_object}
    return render(request,'search.html', context)

@login_required()
def article_create_view(request):
    # form = ArticleForm() # form to be displayed on GET request
    # context = {"form":form}
    # if request.method == "POST":
    #     form = ArticleForm(request.POST)
    #     context['form'] = form
    #     if form.is_valid():
    #         title = form.cleaned_data.get('title') 
    #         content = form.cleaned_data.get('content')
    #         article = Article.objects.create(title=title, content=content)
    #         context['created'] = True
    #         context['article'] = article
    # return render(request,'create.html',context) 
    
    #<!>-- the newer version of the above code is as below#

    form = ArticleForm(request.POST or None) # form to be displayed on GET request
    context = {"form":form}
    
    if form.is_valid():
        article = form.save()
        '''
            title = form.cleaned_data.get('title') 
            content = form.cleaned_data.get('content')
            article = Article.objects.create(title=title, content=content)
        '''
        context['created'] = True
        context['article'] = article
    return render(request,'create.html',context) 