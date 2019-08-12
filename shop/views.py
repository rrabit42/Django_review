from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Item


def item_list(request):
  qs = Item.objects.all()

  # q가 없으면 빈문자열 받아오겠다
  q = request.GET.get('q', '')
  if q:
    #icontains : ignore case 대소문자 구분x
    qs = qs.filter(name__icontains=q)
  
  return render(request, 'shop/item_list.html', {
    'item_list' : qs,
    #검색어 보존
    'q' : q
  })
