from django import forms
from .models import Item

# class ItemForm(forms.Form):
#     name = forms.CharField()
#     desc = forms.CharField(widget=forms.Textarea)

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'  # 이렇게 하면 위처럼 필드 각각 정의 안해도 됨 (admin에서 같은 방식 사용, 물론 custom도 가능)

