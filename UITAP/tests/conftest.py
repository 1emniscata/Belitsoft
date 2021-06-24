from selenium.webdriver import Chrome
import pytest



@pytest.fixture
def browser():
  # capabilities = {
  #   "browserName": "UNKNOWN",
  #   "browserVersion": "",
  #   "selenoid:options": {
  #     "enableVNC": True,
  #     "enableVideo": False
  #   }
  # }
  # driver = webdriver.Remote(
  #   command_executor="http://127.0.0.1:4444//wd/hub",
  #   desired_capabilities=capabilities)
  driver = Chrome()
  driver.implicitly_wait(10)
  yield driver
  driver.quit()

