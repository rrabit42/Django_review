from django.conf import settings
from django.db import models
from askcompany.utils import uuid_upload_to

class Post(models.Model):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(upload_to=uuid_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    # on_delete옵션은 foreignkey로 post와 연결되어 있는데
    # 만약 post가 없어지면 이 comment model도 삭제할 것인지 여부를 결정하는 것
    # cascade는 같이 삭제하겠다는 옵션
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
