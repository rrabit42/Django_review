from django.contrib import admin
from .models import Item

#기본 모델 admin으로 동작
#admin.site.register(Item)

#admin 모델 커스텀 가능
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'short_desc', 'price', 'is_publish']
    list_display_links = ['name', 'short_desc']
    list_filter = ['is_publish', 'updated_at']
    # search는 OR query로 들어감
    search_fields = ['name', 'desc']

    def short_desc(self, item):
        return item.desc[:20]

