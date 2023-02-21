from django.forms import forms,ModelForm
from django.contrib.auth.models import User
from .models import Imagen

class FormularioUser(ModelForm):
    class Meta:
        model = User
        fields = ['username',]


class ImgFormu(ModelForm):
    class Meta:
        model = Imagen
        fields = ['usuario','imagen']