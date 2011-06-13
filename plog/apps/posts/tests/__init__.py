from django.test import TestCase

from ..models import Post

class PostsTestCase(TestCase):
    def create_post(self, **kwargs):
        defaults = {
            'title': 'A Post',
            'slug': 'a-post',
            'html': '<h1>Some HTML</h1>',
        }
        defaults.update(kwargs)
        post = Post(**defaults)
        post.save()
        return post

