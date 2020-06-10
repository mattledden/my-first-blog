from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='C:/Users/Matt/bridge/Testing/geckodriver.exe')

    def tearDown(self):
        self.browser.quit()

    #test buttons appear for viewing/writing/editing

    def test_can_make_cv(self):
        # Edith has heard about a cool new online blog. She goes
        # to check out its homepage
        self.browser.get('http://127.0.0.1:8000/cv/new')

        # She notices the page title and header mention a blog
        self.assertIn('Blog', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('CV', header_text)
        
        #She is invited to enter qualifications
        inputbox = self.browser.find_element_by_id('id_new_qual')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a qualification'
        )
        # She types "GCSE Maths Grade A"
        inputbox.send_keys('GCSE Maths Grade A')
        
        # When she hits enter, the page updates, and now the page lists
        # "GCSE Maths Grade A" as a qualification
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

    def test_can_read_cv(self):
        # Edith has heard about a cool new online blog. She goes
        # to check out its homepage
        self.browser.get('http://127.0.0.1:8000/cv')

        # She notices the page title and header mention a blog
        self.assertIn('Blog', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('CV', header_text)

    def test_can_edit_cv(self):
        # Edith has heard about a cool new online blog. She goes
        # to check out its homepage
        self.browser.get('http://127.0.0.1:8000/cv/edit')

        # She notices the page title and header mention a blog
        self.assertIn('Blog', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('CV', header_text)

        #edit stuff

if __name__ == '__main__':  
    unittest.main(warnings='ignore')