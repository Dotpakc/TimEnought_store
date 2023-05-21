from django.test import TestCase, Client
from django.urls import reverse
from apps.blog.models import BlogCategory, Article


class BlogViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.сategory = BlogCategory.objects.create(name='Category')

    def test_blog_category_list(self):
        response = self.client.get(reverse('blog_category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/category/list.html')
        self.assertContains(response, self.сategory.name)

    def test_article_list(self):
        article = Article.objects.create(title='Article', сategory=self.сategory)
        response = self.client.get(reverse('article_list', args=[self.сategory.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/article/list.html')
        self.assertContains(response, article.title)
