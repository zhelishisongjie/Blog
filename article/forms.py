from django import forms
from mdeditor.widgets import MDEditorWidget
from .models import Article

class ArticleForm(forms.ModelForm):
    '''
    class Meta:                         # 指明数据来源
        model = Article                 # 数据模型来源
        fields = '__all__'
        # fields = ("title" , "body")     # 表单包含的字段
    '''

    body = forms.CharField(widget=MDEditorWidget())
    class Meta:
        model = Article
        fields = ['title', 'body']