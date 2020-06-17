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
        self.browser.get('http://127.0.0.1:8000')

        #She needs to login so clicks the padlock button
        inputbox = self.browser.find_element_by_id("id_login")
        inputbox.send_keys(Keys.ENTER)

        time.sleep(0.5)
        inputbox = self.browser.find_element_by_id('id_username')
        
        inputbox.send_keys('USERNAME')

        inputbox = self.browser.find_element_by_id('id_password')
        
        inputbox.send_keys('PASSWORD') #I haven't put the actual password here as I don't want to upload it to GitHub!! 
        inputbox.send_keys(Keys.ENTER)

        time.sleep(0.5)

        #she sees a link called "CV" and clicks on it
        inputbox = self.browser.find_element_by_id('id_cv')
        inputbox.send_keys(Keys.ENTER)

        time.sleep(0.5)

        # She notices the page header mentions a cv
        header_text = self.browser.find_element_by_id('id_name').text  
        self.assertIn('CV', header_text)

        #she sees a button for writing a new cv so she clicks it
        inputbox = self.browser.find_element_by_id('id_new')
        inputbox.send_keys(Keys.ENTER)

        time.sleep(0.5)

        # She notices the page title mentions a blog and the header mentions a CV
        self.assertIn('Blog', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h2').text  
        self.assertIn('CV', header_text)
        
        #She is invited to enter her name
        inputbox = self.browser.find_element_by_id('id_name')
        
        # She types "Edith"
        inputbox.send_keys('Edith')

        #She is invited to enter her location
        inputbox = self.browser.find_element_by_id('id_location')
        
        # She types "Birmingham"
        inputbox.send_keys('Birmingham')

        #She is invited to enter her age
        inputbox = self.browser.find_element_by_id('id_age')
        
        # She types "22"
        inputbox.send_keys('22')

        #She is invited to enter her contact details
        inputbox = self.browser.find_element_by_id('id_contact')
        
        # She types "999, edith@gmail.com"
        inputbox.send_keys('999, edith@gmail.com')

        #She is invited to enter a profile
        inputbox = self.browser.find_element_by_id('id_profile')
        
        # She types "This is my profile"
        inputbox.send_keys('This is my profile')

        #She is invited to enter her experience
        inputbox = self.browser.find_element_by_id('id_experience')
        
        # She types "lots"
        inputbox.send_keys('lots')

        #She is invited to enter her qualifications
        inputbox = self.browser.find_element_by_id('id_qualifications')
        
        # She types "GCSE Maths Grade A"
        inputbox.send_keys('GCSE Maths Grade A')

        #She is invited to enter her hobbies
        inputbox = self.browser.find_element_by_id('id_hobbies')
        
        # She types "Singing"
        inputbox.send_keys('Singing')

        #She is invited to enter her references
        inputbox = self.browser.find_element_by_id('id_references')
        
        # She types "on request"
        inputbox.send_keys('On request')

        inputbox = self.browser.find_element_by_id('id_submit')

        #when she clicks the save button the form is submitted and she is redirected to the page displaying her CV
        inputbox.send_keys(Keys.ENTER)  

        time.sleep(0.5)

        #she is redirected to a page displaying her CV
        header_text = self.browser.find_element_by_id('id_name').text  
        self.assertIn('Edith', header_text)

    def test_can_read_cv(self):
        # Edith has uploaded her cv to this website
        self.browser.get('http://127.0.0.1:8000')

        #she sees a link called "CV" and clicks on it
        inputbox = self.browser.find_element_by_id('id_cv')
        inputbox.send_keys(Keys.ENTER)

        time.sleep(0.5)
        # She notices the page header mentions her name
        header_text = self.browser.find_element_by_id('id_name').text  
        self.assertIn('Edith', header_text)

    def test_can_edit_cv(self):
        # Edith wants to edit her cv so she goes to the homepage
        self.browser.get('http://127.0.0.1:8000')

        #She needs to login so clicks the padlock button
        inputbox = self.browser.find_element_by_id("id_login")
        inputbox.send_keys(Keys.ENTER)

        time.sleep(0.5)
        inputbox = self.browser.find_element_by_id('id_username')
        
        inputbox.send_keys('USERNAME')

        inputbox = self.browser.find_element_by_id('id_password')
        
        inputbox.send_keys('PASSWORD') #I haven't put the actual password here as I don't want to upload it to GitHub!! 
        inputbox.send_keys(Keys.ENTER)

        time.sleep(0.5)

        #she sees a link called "CV" and clicks on it
        inputbox = self.browser.find_element_by_id('id_cv')
        inputbox.send_keys(Keys.ENTER)

        time.sleep(0.5)

        # She notices the page header mentions a cv
        header_text = self.browser.find_element_by_id('id_name').text  
        self.assertIn('CV', header_text)

        #she sees a button for writing a new cv so she clicks it
        inputbox = self.browser.find_element_by_id('id_edit')
        inputbox.send_keys(Keys.ENTER)

        time.sleep(0.5)

        #She adds her surname to make the cv more professional
        inputbox = self.browser.find_element_by_id('id_name')
        
        # She types " Smith"
        inputbox.send_keys(' Smith')

        #She has moved house so changes her location
        inputbox = self.browser.find_element_by_id('id_location')
        
        # She clears the input box then types "London"
        inputbox.clear()
        inputbox.send_keys('London')

        #She is another year older so updates her age
        inputbox = self.browser.find_element_by_id('id_age')
        
        # She replaces the second 2 with a 3
        inputbox.send_keys(Keys.BACKSPACE)
        inputbox.send_keys('3')

        #She has completed more qualifications
        inputbox = self.browser.find_element_by_id('id_qualifications')
        
        # She enters a new line then types "GCSE English Grade A"
        inputbox.send_keys(Keys.ENTER)
        inputbox.send_keys('GCSE English Grade A')

        time.sleep(2)

        inputbox = self.browser.find_element_by_id('id_submit')

        #when she clicks the save button the form is submitted and she is redirected to the page displaying her updated CV
        inputbox.send_keys(Keys.ENTER)

        time.sleep(0.5)

        #she is redirected to a page displaying her updated CV
        header_text = self.browser.find_element_by_id('id_name').text  
        self.assertIn('Smith', header_text)

        time.sleep(2)
        

if __name__ == '__main__':  
    unittest.main(warnings='ignore')