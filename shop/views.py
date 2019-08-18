import logging
import re

from django.shortcuts import render, get_object_or_404, redirect
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

#인자는 url, 즉, get요청으로부터 받는 듯..?
def item_detail(request, pk):
  item = get_object_or_404(Item, pk=pk)
  return render(request, 'shop/item_detail.html', {
    'item' : item,
  })


# 장고 form을 안쓰면 이렇게 힘들다
def item_new(request, item=None):
  error_list = []
  initial = {}

  if request.method == 'POST':
    data = request.POST
    files = request.FILES

    # 값 한개 가져옴, data.getlist써야 여러개 가져옴
    name = data.get('name')
    desc = data.get('desc')
    price = data.get('price')
    photo = files.get('photo')
    # publish의 값이 이 중 하나면! 값으로 쓰겠다.
    is_publish = data.get('is_publish') in (True, 't', 'True', '1')

    # 유효성 검사(form 안써서...)
    if len(name) < 2:
      error_list.append('name을 2글자 이상 입력해주세요.')

    # 정규표현식임, if 숫자와 대소문자, 그리고 공백으로 표현이 되어있다면~
    if re.match(r'^[\da-zA-Z\s]+$', desc):
      error_list.append('한글을 입력해주세요.')

    #에러가 없다면
    if not error_list:
      # 저장 시도
      if item is None:
        item = Item()

      item.name = name
      item.desc = desc
      item.price = price
      item.is_publish = is_publish

      if photo:
        item.photo.save(photo.name, photo, save=False)

      try:
        item.save()
      except Exception as e:
        error_list.append(e)
      else:
        return redirect(item) # item.get_absolute_url
        # redirect('shop:item_list')와 같음

    initial = {
      'name': name,
      'desc': desc,
      'price': price,
      'photo': photo,
      'is_publish': is_publish,
    }

  else:
    if item is not None:
      initial = {
        'name': item.name,
        'desc': item.desc,
        'price': item.price,
        'photo': item.photo,
        'is_publish': item.is_publish,
      }

  return render(request, 'shop/item_form.html', {
    'error_list': error_list,
    'initial': initial,
  })


def item_edit(request, pk):
  item = get_object_or_404(Item, pk=pk)
  return item_new(request, item)

