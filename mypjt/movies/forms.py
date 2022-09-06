from django import forms
from .models import movies_info

# 그냥 form으로 만드는 경우
# class NewForm(forms.Form):
#     class Meta:
#         model = movies_info
#         fields = '__all__'
#         exclude = ('title',)
#     genre_list = [("공포", "공포"),("스릴러", "스릴러"),("액션", "액션"),("드라마", "드라마")]
#     title = forms.CharField()
#     audience = forms.IntegerField()
#     release_date = forms.DateField()
#     genre = forms.ChoiceField(choices=genre_list)
#     score = forms.DecimalField()
#     poster_url = forms.URLField()
#     description = forms.CharField(widget = forms.Textarea)

# ModelForm 자체를 가져오는 경우
class NewForm(forms.ModelForm):
    
    class Meta:
        model = movies_info
        fields = '__all__'
        

