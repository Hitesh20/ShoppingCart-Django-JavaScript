from django import forms

from .models import Product, Article

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title', 'description', 'price'
        ]


#using form fields in this
class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Add Title'})) #arguments are not necessary.... they have some default values...
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class":"new class", "rows": 30, "cols":100, 'id':'nwId'}))
    price = forms.DecimalField(initial=29.99)



#in this i got all the things/validations/changes mentioned in 2 class and used the first form as basis... this is far more convinient
class ProductForm_Shortcut(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Add Title'})) #arguments are not necessary.... they have some default values...
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={"class": "new class", "rows": 30, "cols": 100, 'id': 'nwId'}))
    price = forms.DecimalField(initial=29.99)
    class Meta:
        model = Product
        fields = [
            'title', 'description', 'price'
        ]

    #this function is to validate title.... that is if we want some custom validation or logic
    #def clean_<my_filed_name>(self, *args, **kwargs):
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')    #to get title
        if 'abc' not in title:
            raise forms.ValidationError('Not a valid title')
        else:
            return title



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title', 'description', 'summary'
        ]