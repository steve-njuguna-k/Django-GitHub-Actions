from django.test import TestCase
from .models import Posts

# Create your tests here.
class TestPostModel(TestCase):    
    def test_post_model(self):
        post = Posts.objects.create(title='Post title', content='This is a post content')
        self.assertTrue(isinstance(post, Posts))

    def test_post_title(self):
        post = Posts.objects.create(title='Post title', content='This is a post content')
        self.assertEqual(str(post.title), 'Post title')
    
    def test_post_content(self):
        post = Posts.objects.create(title='Post title', content='This is a post content')
        self.assertEqual(str(post.content), 'This is a post content')