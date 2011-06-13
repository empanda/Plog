import datetime

from django.db import IntegrityError

from . import PostsTestCase
from ..models import Post


class TestPostCreation(PostsTestCase):
    def test_posts_should_be_creatable(self):
        """Posts should be able to be created."""
        post = self.create_post()

        assert post.id > 0, \
            "The post should have a positive ID."

    def test_posts_should_track_their_creation(self):
        """Posts should track their creation time."""
        before_creation = datetime.datetime.now()
        post = self.create_post()

        assert type(post.created) == datetime.datetime, \
            "The post's created field should be a datetime."

        assert post.created > before_creation, \
            "The post should be created after the earlier datetime."

    def test_posts_should_track_their_modification(self):
        """Posts should track their modification time."""
        post = self.create_post()
        originally_modified = post.modified

        post.html = '<h1>Modified HTML</h1>'
        post.save()

        assert type(post.modified) == datetime.datetime, \
            "The post's modified field should be a datetime."

        assert post.modified > originally_modified, \
            "The post's modified field should update when the post is modified."

    def test_posts_should_have_unique_slugs(self):
        """Posts should have unique slugs."""
        post = self.create_post()
        self.assertRaises(IntegrityError, self.create_post)

    def test_posts_should_return_their_title_when_stringified(self):
        """Posts should return their title when stringified"""
        post = self.create_post()

        assert unicode(post) == post.title, \
            "A stringified post should return it's title."


class TestPostQueryset(PostsTestCase):
    def test_posts_should_be_ordered_by_their_created_date(self):
        """Posts should be ordered by their created date."""
        post1 = self.create_post()
        post2 = self.create_post(title='a second post', slug='a-second-post')

        posts = list(Post.objects.all())
        assert posts == [post2, post1], \
            "Post should be ordered by newest first."


class TestPostAdmin(PostsTestCase):
    def test_post_admin_changelist_view_should_load(self):
        """The Post admin changelist view should load."""
        post = self.create_post()
        self.assertAdminViewLoads('posts', 'post', 'changelist')

    def test_post_admin_add_view_should_load(self):
        """The Post admin add view should load."""
        self.assertAdminViewLoads('posts', 'post', 'add')

    def test_post_admin_change_view_should_load(self):
        """The Post admin change view should load."""
        post = self.create_post()
        self.assertAdminViewLoads('posts', 'post', 'change', args=[post.id])
