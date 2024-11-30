import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLinksInHomepage:
    def setup_method(self):
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        self.driver.quit()

    def helper_test_link(self, link_text, element_selector):
        self.driver.get("https://ultimateqa.com/automation/")
        self.driver.set_window_size(1552, 832)
        self.driver.find_element(By.LINK_TEXT, link_text).click()
        time.sleep(2)
        elements = self.driver.find_elements(By.CSS_SELECTOR, element_selector)
        assert len(elements) > 0

    def test_link1(self):
        self.helper_test_link("Big page with many elements", "#Section_of_Buttons")

    def test_link2(self):
        self.helper_test_link("Fake Landing Page", ".et_pb_text_0 h1")

    def test_link3(self):
        self.helper_test_link("Fake Pricing Page", "h1")

    def test_link4(self):
        self.helper_test_link("Fill out forms", "#et_pb_contact_name_0")

    def test_link5(self):
        self.helper_test_link("Learn how to automate an application that evolves over time", "h2:nth-child(1)")
