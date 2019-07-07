
from .models import Shoes,Suggestions

class ShoesForm(forms.ModelForm):
    class Meta:
        model=Shoes
        fields=['shoes_title','shoes_body','shoes_image']

class Suggestions(forms.ModelForm):
    class Meta:
        model=Suggestions
        fields=['title','body']




