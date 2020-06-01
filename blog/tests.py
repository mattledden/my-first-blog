from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from blog.views import post_list

class PostListTest(TestCase):

    def test_root_url_resolves_to_post_list_view(self):
        found = resolve('/')
        self.assertEqual(found.func, post_list)

    
    def test_post_list_returns_correct_html(self):
        request = HttpRequest()
        response = post_list(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('\n<html>'))
        self.assertIn("<title>Matt's blog</title>", html)
        self.assertTrue(html.endswith('</html>'))
