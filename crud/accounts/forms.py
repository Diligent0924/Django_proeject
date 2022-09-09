from django.contrib.auth.forms import UserCreationForm, UserChangeForm # Substitute 생성 함수
from django.contrib.auth import get_user_model # from .models import User를 직접 참조하지 않기 위해서 django에서 만든 함수

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta): # 상위 Meta를 상속받아서
        model = get_user_model() # Substitute Database를 들고온다.
        fields =  UserCreationForm.Meta.fields + ('email','date_joined')

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('username','email')