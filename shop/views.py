import logging
import re

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, request
from django.views.generic import CreateView, UpdateView
from .models import Item
from .forms import ItemForm

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

#인자는 url, 즉, get요청으로부터 받는 듯..?
def item_detail(request, pk):
  item = get_object_or_404(Item, pk=pk)
  return render(request, 'shop/item_detail.html', {
    'item' : item,
  })


# # 장고 form을 안쓰면 이렇게 힘들다
# def item_new(request, item=None):
#   if request.method == 'POST':
#     form = ItemForm(request.POST, request.FILES, instance=item)   # 순서 바꾸면 안됨
#     if form.is_valid():
#       item = form.save()   # ModelForm에서 제공해주는 기능
#       return redirect(item)
#
#   else: #GET 요청일 때
#     form = ItemForm(instance=item)  #instance도 ModelForm에서 지원, edit 구현 위해 넘겨준다
#
#   return render(request, 'shop/item_form.html', {
#     'form' : form,
#   })
#
#
# def item_edit(request, pk):
#   item = get_object_or_404(Item, pk=pk)
#   return item_new(request, item)


# 얘네 내부 코드가 위에 있는 것들
# 나중 코스에서 다룬다
item_new = CreateView.as_view(model=Item, form_class=ItemForm)
item_edit = UpdateView.as_view(model=Item, form_class=ItemForm)

