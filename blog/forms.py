from django import forms

from blog.models import Photo, Blog

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image', 'caption')

class BlogForm(forms.ModelForm):
    edit_blog = forms.CharField(
        widget=forms.HiddenInput, 
        initial=True
    )
    
    class Meta:
        model = Blog
        fields = ("title", "content")


class DeleteBlogForm(forms.Form):
    
    delete_blog = forms.CharField(
        widget=forms.HiddenInput, 
        initial=True
    )
