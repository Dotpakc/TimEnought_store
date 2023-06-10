from django import forms

from .models import Comment, Article

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
        
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('category', 'tags', 'title', 'slug', 'content_preview', 'content', 'status', 'image')