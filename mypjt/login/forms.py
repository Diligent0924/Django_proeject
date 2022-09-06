# HTML에서 forms를 django form으로 만드는 과정
from django import forms
from .models import Login


# HTML안에 넣어주면서 조회만 하는 경우에는 Form을 사용한다.
class LoginForm(forms.Form):
    id = forms.CharField()
    password = forms.CharField()

class plusForm(forms.ModelForm):
    # 변수 이름과 fields 안에 있는 변수 이름이 같아야 매칭 된다.
    verify_id = forms.CharField(
        label='아이디',
        # 단순히 input tag의 표현정도를 조절만 한다.
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control', # 여기서 bootstrap을 사용
                'placeholder' : 'Write ID',
                'maxlength' : 10,
            }
        ),
        error_messages= {
            'required' : 'Please enter your id'
        }
    )
    
    password = forms.CharField(
        label='비밀번호',
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Write password',
                'maxlength' : 10,
            }
        ),
        error_messages= {
            'required' : 'Please enter your password'
        }
    )
    class Meta:
        model = Login
        fields = "__all__"
        