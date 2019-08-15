import logging
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, request
from .models import Item

logger = logging.getLogger(__name__)  # __name__ => "shop.views"
                                      #즉, settings.py에서 loggers에 추가해줘야함

def item_list(request):
  qs = Item.objects.all()

  # q가 없으면 빈문자열 받아오겠다
  q = request.GET.get('q', '')
  if q:
    #icontains : ignore case 대소문자 구분x
    qs = qs.filter(name__icontains=q)

  logger.debug('query : {}'.format(q))
  
  return render(request, 'shop/item_list.html', {
    'item_list' : qs,
    #검색어 보존
    'q' : q
  })


def item_detail(request, pk):
  item = get_object_or_404(Item, pk=pk)
  return render(request, 'shop/item_detail.html', {
    'item' : item,
  })