import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseTest:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Edge()
        self.driver.get("https://ultimateqa.com/automation")
        self.driver.set_window_size(1536, 816)
    
    def teardown_method(self, method):
        self.driver.quit()

class TestInteractiveElements(BaseTest):
    def _navigate_to_interactions(self):
        # Wait until the link is clickable and then click it
        wait = WebDriverWait(self.driver, 10)
        interactions_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Interactions with simple elements")))
        interactions_link.click()

    def test_button_success(self):
        self._navigate_to_interactions()
        
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.ID, "idExample")))
        button.click()

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".entry-title")))
        assert self.driver.find_element(By.CSS_SELECTOR, ".entry-title").text == "Button success"

    def test_checkbox(self):
        self._navigate_to_interactions()
        # Wait for the checkbox to be clickable and then click it
        wait = WebDriverWait(self.driver, 10)
        checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".et_pb_blurb_7 input:nth-child(3)")))
        checkbox.click()

        assert checkbox.is_selected()

    def test_link_success(self):
        self._navigate_to_interactions()

        wait = WebDriverWait(self.driver, 10)
        link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Click me using this link text!")))
        link.click()

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".entry-title")))
        assert self.driver.find_element(By.CSS_SELECTOR, ".entry-title").text == "Link success"
    
    def test_radio_button(self):
        self._navigate_to_interactions()
        
        # Wait for the radio button to be clickable
        wait = WebDriverWait(self.driver, 10)
        radio_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".et_pb_blurb_6 input:nth-child(3)")))

        # Scroll the page to the radio button
        self.driver.execute_script("arguments[0].scrollIntoView();", radio_button)
        time.sleep(3)

        radio_button.click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".et_pb_blurb_6 input:nth-child(3)")))

        assert radio_button.is_selected(), "Radio button was not selected"



    def test_dropdown_options(self):
        self._navigate_to_interactions()
        # Scroll to the dropdown
        self.driver.execute_script("window.scrollTo(0, 321.6)")
        
        # Wait for the dropdown to be clickable and then click it
        wait = WebDriverWait(self.driver, 10)
        dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select")))
        dropdown.click()

        # Wait for the option to be clickable and then select it
        option = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[. = 'Opel']")))
        option.click()
