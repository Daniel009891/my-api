from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostslistsViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='phil', password='pass')

    def test_can_list_posts(self):
        phil = User.objects.get(username='phil')
        Post.objects.create(owner=phil, title='a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='phil', password='pass')
