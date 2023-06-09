from django import forms

from .models import Comment, Article

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}), # 'type': 'email
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }
        
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'slug', 'content_preview', 'content', 'status', 'image', 'category', 'tags')
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control ckeditor'})
        }