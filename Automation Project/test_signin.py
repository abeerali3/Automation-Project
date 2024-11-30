import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSignIn():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Edge()
        self.driver.set_window_size(1536, 816)

    def teardown_method(self):
        self.driver.quit()

    def wait_for_element(self, by, value):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))

    def login(self, email, password):
        self.driver.find_element(By.LINK_TEXT, "Sign In").click()
        self.wait_for_element(By.ID, "user[email]").send_keys(email)
        self.driver.find_element(By.ID, "user[password]").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, ".button-primary").click()


    def test_signin_empty_email_field(self):
        self.driver.get("https://courses.ultimateqa.com/collections")
        self.driver.find_element(By.LINK_TEXT, "Sign In").click()
        self.driver.find_element(By.ID, "user[password]").click()
        assert len(self.driver.find_elements(By.ID, "user[email]-error")) > 0

    def test_signin_empty_password_field(self):
        self.driver.get("https://courses.ultimateqa.com/collections")
        self.driver.find_element(By.LINK_TEXT, "Sign In").click()
        self.driver.find_element(By.ID, "user[email]").send_keys("abcde@abcd.com")
        self.driver.find_element(By.ID, "user[password]").click()
        assert len(self.driver.find_elements(By.ID, "user[password]-error")) > 0

    def test_signin_wrong_email(self):
        self.driver.get("https://ultimateqa.com/automation")
        self.driver.find_element(By.LINK_TEXT, "Free Courses").click()
        self.login("ab@ab.com", "qastudenttpassword")
        time.sleep(4)
        assert len(self.driver.find_elements(By.CSS_SELECTOR, ".form-error__list-item")) > 0

    def test_signin_success(self):
        self.driver.get("https://ultimateqa.com/automation")
        self.driver.find_element(By.LINK_TEXT, "Free Courses").click()
        self.login("abcde@abcd.com", "qastudenttpassword")
        time.sleep(4)
        assert len(self.driver.find_elements(By.ID, "my-courses-heading")) > 0
        
        
    def test_forgot_password(self):
          self.driver.get("https://courses.ultimateqa.com/users/sign_in")
          self.driver.set_window_size(1528, 816)
          self.driver.find_element(By.ID, "user[email]").click()
          self.driver.find_element(By.ID, "user[email]").send_keys("abcde@abcd.com")
          self.driver.find_element(By.LINK_TEXT, "Forgot Password?").click()
          self.driver.find_element(By.ID, "user[email]").click()
          self.driver.find_element(By.ID, "user[email]").send_keys("abcde@abcd.com")
          self.driver.find_element(By.NAME, "commit").click()
          elements = self.driver.find_elements(By.CSS_SELECTOR, ".password-reset__heading")
          assert len(elements) > 0
  

  
