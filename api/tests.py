from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Post


class PostTest(APITestCase):
    def test_list(self):
        """
        retrieve list of all posts
        """
        url = reverse('post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        """
        create post
        """
        url = reverse('post-list')
        data = {'text': 'test'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().text, 'test')

    def test_update(self):
        """
        update post
        """
        created = Post.objects.create(text='test')
        url = reverse('post-detail', kwargs={'pk': created.id})
        data = {'text': 'test2'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().text, 'test2')

    def test_delete(self):
        """
        delete post
        """
        created = Post.objects.create(text='test')
        url = reverse('post-detail', kwargs={'pk': created.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)
