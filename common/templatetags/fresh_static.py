from time import time
from django import template
from django.conf import settings
from django.templatetags.static import StaticNode

register = template.Library()


# StaticNode 상속
class FreshStaticNode(StaticNode):
    def url(self, context):
        url = super().url(context)
        # 개발모드일때만
        # 보통 의미없는 더미스트링에는 _를 붙임
        if settings.DEBUG:
            url += '?_={}'.format(int(time()))
        return url


# 실제 static tag로 등록
@register.tag('fresh_static')
def do_static(parser, token):
    return FreshStaticNode.handle_token(parser, token)

