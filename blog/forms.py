from django import forms

from .models import Comment, Article, Tag

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
    tags_input = forms.CharField(max_length=100, label='Теги', help_text='Введіть теги через кому', required=False)
    class Meta:
        model = Article
        fields = ('category', 'tags_input', 'title', 'slug', 'content_preview', 'content', 'status', 'image')
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control ckeditor'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:  # Проверяем, редактируется ли статья (есть ли у нее первичный ключ)
            tags = ', '.join(self.instance.tags.values_list('name', flat=True))
            self.initial['tags_input'] = tags

    def save(self, commit=True):
        article = super().save(commit=False)
        if commit:
            article.save()
        tags = self.cleaned_data['tags_input']
        tags_list = [tag.strip() for tag in tags.split(',')]
        for tag in tags_list:
            tag_obj, created = Tag.objects.get_or_create(name=tag)
            article.tags.add(tag_obj)
        return article
    