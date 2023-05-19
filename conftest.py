import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

"""Fixture for create and open driver in set up stage  and close it in tear down stage.
scope=function for every test"""


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())              # create driver
    driver.maximize_window()                                                # maximize window
    yield driver                                                            # works as a return
    driver.quit()                                                           # close browser
