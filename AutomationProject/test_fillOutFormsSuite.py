import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestFillOutFormsSuite():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Edge()
        self.vars = {}
    
    def teardown_method(self, method):
        self.driver.quit()

    def test_emptynamefield(self):
        self.driver.get("https://ultimateqa.com/automation")
        self.driver.set_window_size(1552, 832)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Fill out forms"))).click()
        message_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "et_pb_contact_message_0")))
        message_field.click()
        message_field.send_keys("Hello World! This is a QA student ")

        submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "et_builder_submit_button")))
        submit_button.click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "et_builder_submit_button")))

        # Use ActionChains to move to the element
        actions = ActionChains(self.driver)
        actions.move_to_element(submit_button).perform()
        body_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body")))
        actions.move_to_element_with_offset(body_element, 0, 0).perform()
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".et-pb-contact-message li")))
        time.sleep(3)
        assert len(elements) > 0

    def test_emptyfields(self):
        self.driver.get("https://ultimateqa.com/automation")
        self.driver.set_window_size(1552, 832)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Fill out forms"))).click()
        submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "et_builder_submit_button")))
        submit_button.click()
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".et-pb-contact-message > p")))
        assert len(elements) > 0

    def test_fillinformsuccess(self):
        self.driver.get("https://ultimateqa.com/automation")
        self.driver.set_window_size(1552, 832)

        # Wait for the 'About' link and move to it
        about_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "About")))
        actions = ActionChains(self.driver)
        actions.move_to_element(about_link).perform()
        body_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body")))
        actions.move_to_element_with_offset(body_element, 0, 0).perform()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Fill out forms"))).click()
        name_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "et_pb_contact_name_0")))
        name_field.click()
        name_field.send_keys("Hello World")

        message_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "et_pb_contact_message_0")))
        message_field.click()
        message_field.send_keys("This is a QA student")

        submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "et_builder_submit_button")))
        submit_button.click()

        # Wait for the submit button to be interactable (for the move action)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "et_builder_submit_button")))
        actions.move_to_element(submit_button).perform()

        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".et-pb-contact-message > p")))
        time.sleep(3)
        assert len(elements) > 0

    def test_invalidname(self):
        self.driver.get("https://ultimateqa.com/automation")
        self.driver.set_window_size(1552, 832)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Fill out forms"))).click()
        name_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "et_pb_contact_name_0")))
        name_field.click()
        name_field.send_keys("&^%")
        message_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "et_pb_contact_message_0")))
        message_field.click()
        message_field.send_keys("This is a test!")
        time.sleep(3)

        submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "et_builder_submit_button")))
        submit_button.click()

        # Wait for and check if error message appears
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".et-pb-contact-message > p")))
        text = self.driver.find_element(By.CSS_SELECTOR, ".et-pb-contact-message > p").text
        assert text != "Thanks for contacting us"

    def test_messageTooShort(self):
        self.driver.get("https://ultimateqa.com/automation")
        self.driver.set_window_size(1552, 832)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Fill out forms"))).click()
        name_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "et_pb_contact_name_0")))
        name_field.click()
        name_field.send_keys("Hello World")

        message_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "et_pb_contact_message_0")))
        message_field.click()
        message_field.send_keys("a")
        time.sleep(2)
        submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "et_builder_submit_button")))
        submit_button.click()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".et-pb-contact-message > p")))
        time.sleep(3)
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".et-pb-contact-message > p")
        assert all(element.text != "Thanks for contacting us" for element in elements)

