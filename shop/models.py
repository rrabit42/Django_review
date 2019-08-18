from django.conf import settings
from django.db import models
from django.urls import reverse

from askcompany.utils import uuid_upload_to


class Item(models.Model):
  name = models.CharField(max_length=100)
  desc = models.TextField(blank=True)
  photo = models.ImageField(blank=True, upload_to=uuid_upload_to)
  price = models.PositiveIntegerField()
  is_publish = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    # return '<{}> {}'.format(self.pk, self.name)
    return f'<{self.pk}> {self.name}'

  def get_absolute_url(self):
    # args: 튜플, kwargs: 딕셔너리
    # return reverse('shop:item_detail', args=[self.pk])
    # 얘랑 같은 의미
    # shop은 namespace, item_detail은 url에서 name지정해 준 것
    return reverse('shop:item_detail', kwargs={'pk': self.pk})
    # 여기서 'pk'는 urls.py에 있는 <int:pk>의 pk와 맞춰주는 것!

class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    