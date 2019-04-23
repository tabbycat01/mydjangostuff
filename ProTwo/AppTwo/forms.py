from django.forms import ModelForm
from AppTwo.models import Users

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'email']