from django import forms
from .models import *

class AnimalForm(forms.ModelForm):
    name = forms

    # 이 정보를 가지고 Blog Form을 만들겠다
    class Meta:
        model = Animal

        # models.py에 있는 필드들 의미
        # pub_date는 글 작성시간을 자동으로 넣어야 하니까 form 가져오지 마
        fields = ['name','species','subspecies','profile_photo','birthday','memorialday','introduce','season','flowers','gravestone']