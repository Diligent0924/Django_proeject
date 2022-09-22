from django import forms
from .models import ArticleModel, CommentModel

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = ArticleModel
        fields = '__all__'

class CommentForm(forms.ModelForm):
    
    # def __init__(self, *args, **kwargs):
    #     super(CommentForm, self).__init__(*args, **kwargs)
    #     self.fields['comment'].strip = False
    class Meta:
        model = CommentModel
        fields = "__all__"
        exclude = ('article','username')
    # 이러지마 제발..