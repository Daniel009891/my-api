from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostslistsViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='phil', password='pass')

    def test_can_list_posts(self):
        """Testing a user can list posts"""
        phil = User.objects.get(username='phil')
        Post.objects.create(owner=phil, title='a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        """Testing a logged in user can create a post"""
        self.client.login(username='phil', password='pass')
        response = self.client.post('/posts/', {'title': 'a title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        """Testing a logged out user can't create a post"""
        response = self.client.post('/posts/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    def setup(self):
        phil = User.objects.create_user(username='phil', password='pass')

        Post.objects.create(
            owner=phil, title='a title', content='some content'
        )

    def test_can_retrieve_post_using_invalid_id(self):
        """Testing a user can't retrieve a post using invalid ID"""
        response = self.client.get('/posts/87/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

 