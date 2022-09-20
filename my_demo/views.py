from django.http import HttpResponse
from django.template.loader import render_to_string
import random
from articles.models import Article

def home_view(request, *args, **kwargs):
    number = random.randint(1,3)
    article = Article.objects.all()
    context = {
        "object_list": article,
    }
    HTML_STRING = render_to_string("home-view.html",context)
    # HTML_STRING = """
    # <h1>{title} - (id):{id}</h1>
    # <p>{content}</p>
    # """.format(**context)
    return HttpResponse(HTML_STRING)