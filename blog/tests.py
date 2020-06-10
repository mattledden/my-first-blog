from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from blog.views import post_list
from blog.models import CV

class PostListTest(TestCase):
    
    def test_cv_returns_correct_html(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/cv.html', 'blog/base.html')

    def test_edit_cv_returns_correct_html(self):
        response = self.client.get('/cv/edit/')
        self.assertTemplateUsed(response, 'cv/edit_cv.html', 'blog/base.html')

    def test_new_cv_returns_correct_html(self):
        response = self.client.get('/cv/new/')
        self.assertTemplateUsed(response, 'cv/edit_cv.html', 'blog/base.html')

    def test_can_save_a_POST_request(self):
        self.client.post('/cv/new/', data={'name': 'Matt'})

        self.assertEqual(CV.objects.count(), 1)
        new_cv = CV.objects.first()
        self.assertEqual(new_cv.name, 'Matt')

    def test_redirects_after_POST(self):
        response = self.client.post('/cv/new/', data={'name': 'Matt'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/')

    def test_only_saves_cv_when_necessary(self):
        self.client.get('/cv/')
        self.assertEqual(CV.objects.count(), 0)