from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # logon to the site
        self.browser.get('http://localhost:8000')

        # check the title
        self.assertIn('To-Do', self.browser.title)
        
        # check the header on the page
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        
        # Enter todo item 1
        inputbox.send_keys('Buy peacock feathers')
        # Send the input
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        ''' 
        Potentital gotcha: 
        Watch out for the difference between the
        Selenium find_element_by... and find_elements_by... functions. One
        returns an element, and raises an exception if it can’t find it,
        whereas the other returns a list, which may be empty.
        '''
        rows = self.browser.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
