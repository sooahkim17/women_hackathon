from django.shortcuts import render, get_object_or_404, redirect
from bs4 import BeautifulSoup
import requests 
from shoes.models import Suggestions
from django.db.models import Q


from .models import Suggestions,Shoes



# Create your views here.
def home(request):
    return render(request,'home.html')

def suggestion(request):
    suggestions = Suggestions.objects
    return render(request,'suggestion.html',{'suggestions':suggestions})

def suggestion_detail(request, suggestion_id):
    suggestion_detail=get_object_or_404(Suggestions,pk=suggestion_id)
    return render(request,'suggestion_detail.html',{'suggestion':suggestion_detail})

def suggestion_new(request):
    return render(request,'suggestion_new.html')

def create(request):
    suggestion = Suggestions()
    suggestion.title = request.GET['title']
    suggestion.body= request.GET['body']
    suggestion.save()
    return redirect('/suggestion/'+str(suggestion.id))

def delete(request,suggestion_id):
    suggestion_detail = get_object_or_404(Suggestions, pk=suggestion_id)
    suggestion_detail.delete()
    return redirect('/suggestion/')

def edit(request, suggestion_id):
    if (request.method == 'POST'):
        suggestion_detail = get_object_or_404(Suggestions, pk = suggestion_id)
        return render(request,'suggestion_edit.html',{'suggestion':suggestion_detail})

def update(request,suggestion_id):
    suggestion=get_object_or_404(Suggestions, pk=suggestion_id)
    if (request.method == 'POST'):
        suggestion.title = request.POST['title']
        suggestion.body = request.POST['body']
        suggestion.save()
        return redirect('/suggestion/'+str(suggestion.id))


# 검색

def post_list(request):
     qs = Shoes.objects.all()
     q = request.GET.get('q', '') # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
     results=[]
     if q: # q가 있으면
        #title__icontains=q
         qs = qs.filter(shoes_title__icontains=q)
         for object in qs:
             results.append(object)
          # 제목에 q가 포함되어 있는 레코드만 필터링

     return render(request, 'home_detail.html', {'results' : results,'q' : q,})


