from .common import *
# 필요한거는 추가하면 됨

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'askcompany_db',
        'USER': 'root',
        'PASSWORD': 'qwer1234',
        'HOST':'127.0.0.1',
        # 'OPTIONS': {},
    }
}