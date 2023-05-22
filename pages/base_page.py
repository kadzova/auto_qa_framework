from selenium.webdriver.support.ui import WebDriverWait as wait             # "as wait" renames WebDriverWait to wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url


    def open(self):                                    #simply function to open the desired url/page
        self.driver.get(self.url)

    """Args:
         - driver - Instance of WebDriver (Ie, Firefox, Chrome or Remote)
         - timeout - Number of seconds before timing out"""

    """An element is present on the DOM of a page and visible. 
        
        Visibility means that the element is not only displayed
        but also has a height and width that is greater than 0.
        """
    def element_is_visible(self, locator, timeout=5):   # by default timeout for 5 sec
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):   # by default timeout for 5 sec
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    """An element is present on the DOM of a page. 
    This does not necessarily mean that the element is visible.
        """
    def element_is_present(self, locator, timeout=5):   # by default timeout for 5 sec
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_present(self, locator, timeout=5):   # by default timeout for 5 sec
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    """An element is either invisible or not present on the DOM.
        """
    def element_is_not_visible(self, locator, timeout=5):   # by default timeout for 5 sec
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    """An element is visible and enabled such that you can click it.
        """
    def element_is_clickable(self, locator, timeout=5):   # by default timeout for 5 sec
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    """execute_script
           Synchronously Executes JavaScript in the current window/frame.

           :Args:
            - script: The JavaScript to execute.
            - \\*args: Any applicable arguments for your JavaScript.

           :Usage:
               ::

                   driver.execute_script('return document.title;')
           """
    def go_to_element(self, element):
        self.driver.execute_script("argument[0].scrollIntoView();", element)

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('fixedban').style.display='none'")
