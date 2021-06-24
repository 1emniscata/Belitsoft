from selenium.webdriver import Chrome
import pytest



@pytest.fixture
def browser():

  driver = Chrome()
  driver.implicitly_wait(10)
  yield driver
  driver.quit()

