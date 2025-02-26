from django.test import TestCase
from django.urls import reverse

class UrlsTests(TestCase):
    def test_home_url(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)  # Проверяем статус-код


class UrlsTests(TestCase):
    def test_about_url(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url(self):
        response = self.client.get(reverse('post_detail', args=[1]))  # Тестируем маршрут поста с ID 1
        self.assertEqual(response.status_code, 200)