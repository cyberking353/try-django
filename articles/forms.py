from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content']
    
    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error('title', f'\'{title.title()}\' already exist, please pick another title' )



class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    
    # def clean_title(self): #validation methods for validating data in specified field (title)
    # def clean_<fieldname>
    #     cleaned_data = self.cleaned_data #data after calling '.is_valid' method on forms
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == 'this is example':
    #         raise forms.ValidationError('this title already exist.')
    #     print(title)
    #     return title
    
    def clean(self): #validation methods for validating data in all field
        cleaned_data = self.cleaned_data #data after calling '.is_valid' method on forms
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == 'this is example':
            self.add_error('title', 'this title already exist.') #this is an field error (error raise for epecific field)
        if 'example' in content or 'example' in title.lower(): #scenario for using non-field validation error
            self.add_error('title', 'example cannot be in title')
            raise forms.ValidationError('example is not allowed.') #this is a non-field error (error raised for the entire form)
        return cleaned_data

