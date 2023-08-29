from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:                         # 指明数据来源
        model = Article                 # 数据模型来源
        fields = ("title" , "body")     # 表单包含的字段