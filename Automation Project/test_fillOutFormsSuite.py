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

        # Wait for and click the 'Fill out forms' link
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Fill out forms"))).click()

        # Wait for the message field to be clickable, then interact with it
        message_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "et_pb_contact_message_0")))
        message_field.click()
        message_field.send_keys("Hello World! This is a QA student ")

        # Wait for and click the submit button
        submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "et_builder_submit_button")))
        submit_button.click()

        # Wait for the submit button to be interactable (for the move action)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "et_builder_submit_button")))

        # Use ActionChains to move to the element
        actions = ActionChains(self.driver)
        actions.move_to_element(submit_button).perform()

        # Wait for the body to be interactable
        body_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body")))

        # Move to the top-left corner of the body element
        actions.move_to_element_with_offset(body_element, 0, 0).perform()

        # Check if the message was submitted successfully
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".et-pb-contact-message li")))
        assert len(elements) > 0

    def test_emptyfields(self):
        self.driver.get("https://ultimateqa.com/automation")
        self.driver.set_window_size(1552, 832)

        # Wait for and click the 'Fill out forms' link
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Fill out forms"))).click()

        # Wait for the submit button to be clickable, then click it
        submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "et_builder_submit_button")))
        submit_button.click()

        # Wait for the error message to appear
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".et-pb-contact-message > p")))
        assert len(elements) > 0

    def test_fillinformsuccess(self):
        self.driver.get("https://ultimateqa.com/automation")
        self.driver.set_window_size(1552, 832)

        # Wait for the 'About' link and move to it
        about_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "About")))
        actions = ActionChains(self.driver)
        actions.move_to_element(about_link).perform()

        # Move to the body element and then to the top-left corner
        body_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body")))
        actions.move_to_element_with_offset(body_element, 0, 0).perform()

        # Click the 'Fill out forms' link
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Fill out forms"))).click()

        # Wait for the name field, click it, and enter text
        name_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "et_pb_contact_name_0")))
        name_field.click()
        name_field.send_keys("Hello World")

        # Wait for the message field, click it, and enter text
        message_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "et_pb_contact_message_0")))
        message_field.click()
        message_field.send_keys("This is a QA student")

        # Wait for and click the submit button
        submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "et_builder_submit_button")))
        submit_button.click()

        # Wait for the submit button to be interactable (for the move action)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "et_builder_submit_button")))

        # Use ActionChains to move to the element
        actions.move_to_element(submit_button).perform()

        # Wait for the error message to appear after submission
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".et-pb-contact-message > p")))
        assert len(elements) > 0

    def test_invalidname(self):
        self.driver.get("https://ultimateqa.com/automation")
        self.driver.set_window_size(1552, 832)

        # Wait for and click the 'Fill out forms' link
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Fill out forms"))).click()

        # Enter invalid characters for the name field
        name_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "et_pb_contact_name_0")))
        name_field.click()
        name_field.send_keys("&^%")

        # Fill in a message
        message_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "et_pb_contact_message_0")))
        message_field.click()
        message_field.send_keys("This is a test!")

        # Submit the form
        submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "et_builder_submit_button")))
        submit_button.click()

        # Wait for and check if error message appears
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".et-pb-contact-message > p")))

        # Validate that the form does not submit with invalid characters in the name
        text = self.driver.find_element(By.CSS_SELECTOR, ".et-pb-contact-message > p").text
        assert text != "Thanks for contacting us"

    def test_messageTooShort(self):
        self.driver.get("https://ultimateqa.com/automation")
        self.driver.set_window_size(1552, 832)

        # Wait for and click the 'Fill out forms' link
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Fill out forms"))).click()

        # Fill in a valid name
        name_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "et_pb_contact_name_0")))
        name_field.click()
        name_field.send_keys("Hello World")

        # Enter a message that's too short
        message_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "et_pb_contact_message_0")))
        message_field.click()
        message_field.send_keys("a")

        # Submit the form
        submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "et_builder_submit_button")))
        submit_button.click()

        # Wait for and check if error message appears
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".et-pb-contact-message > p")))

        # Ensure no success message appears
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".et-pb-contact-message > p")
        assert len(elements) == 0
