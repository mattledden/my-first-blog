#DISCLAIMER!
#these tests work when I allow the real password to be inputted but obviously I didn't want that to be uploaded to GitHub!!

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
        self.browser.get('http://127.0.0.1:8000/accounts/login/?next=/cv/new')

        #She needs to login
        inputbox = self.browser.find_element_by_id('id_username')
        
        inputbox.send_keys('USERNAME')
        inputbox.send_keys(Keys.TAB)

        inputbox = self.browser.find_element_by_id('id_password')
        
        inputbox.send_keys('PASSWORD') #I haven't put the actual password here as I don't want to upload it to GitHub!! 
        inputbox.send_keys(Keys.ENTER)

        time.sleep(1)

        # She notices the page title and header mention a blog
        self.assertIn('Blog', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h2').text  
        self.assertIn('CV', header_text)
        
        #She is invited to enter her name
        inputbox = self.browser.find_element_by_id('id_name')
        
        # She types "Edith"
        inputbox.send_keys('Edith')
        
        # When she hits tab she can fill in the next field
        inputbox.send_keys(Keys.TAB)

        #She is invited to enter her location
        inputbox = self.browser.find_element_by_id('id_location')
        
        # She types "Birmingham"
        inputbox.send_keys('Birmingham')
        
        # When she hits tab she can fill in the next field
        inputbox.send_keys(Keys.TAB)

        #She is invited to enter her age
        inputbox = self.browser.find_element_by_id('id_age')
        
        # She types "22"
        inputbox.send_keys('22')
        
        # When she hits tab she can fill in the next field
        inputbox.send_keys(Keys.TAB)

        #She is invited to enter her contact details
        inputbox = self.browser.find_element_by_id('id_contact')
        
        # She types "999, edith@gmail.com"
        inputbox.send_keys('999, edith@gmail.com')
        
        # When she hits tab she can fill in the next field
        inputbox.send_keys(Keys.TAB)

        #She is invited to enter a profile
        inputbox = self.browser.find_element_by_id('id_profile')
        
        # She types "This is my profile"
        inputbox.send_keys('This is my profile')
        
        # When she hits tab she can fill in the next field
        inputbox.send_keys(Keys.TAB)

        #She is invited to enter her experience
        inputbox = self.browser.find_element_by_id('id_experience')
        
        # She types "lots"
        inputbox.send_keys('lots')
        
        # When she hits tab she can fill in the next field
        inputbox.send_keys(Keys.TAB)

        #She is invited to enter her qualifications
        inputbox = self.browser.find_element_by_id('id_qualifications')
        
        # She types "GCSE Maths Grade A"
        inputbox.send_keys('GCSE Maths Grade A')
        
        # When she hits tab she can fill in the next field
        inputbox.send_keys(Keys.TAB)

        #She is invited to enter her hobbies
        inputbox = self.browser.find_element_by_id('id_hobbies')
        
        # She types "Singing"
        inputbox.send_keys('Singing')
        
        # When she hits tab she can fill in the next field
        inputbox.send_keys(Keys.TAB)

        #She is invited to enter her references
        inputbox = self.browser.find_element_by_id('id_references')
        
        # She types "on request"
        inputbox.send_keys('On request')

        time.sleep(1)
        
        # When she hits tab she can fill in the next field
        #inputbox.send_keys(Keys.TAB)

        #time.sleep(1)
        inputbox = self.browser.find_element_by_id('id_submit')
        time.sleep(1)
        #when she hits enter the form is submitted and she is redirected to the page displaying her CV
        inputbox.send_keys(Keys.ENTER)

        time.sleep(2)
        

    '''def test_can_read_cv(self):
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
        '''

if __name__ == '__main__':  
    unittest.main(warnings='ignore')