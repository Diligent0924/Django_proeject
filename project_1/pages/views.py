from django.shortcuts import render
from . import database
# Create your views here.
def pages(request, id):
    dic = database.dic
    context = {
        "id" : id,
        "name" : dic[id]['name'],
        "age" : dic[id]['age'],
        "text" : dic[id]['text'],
    }
    return render(request, "pages.html", context)