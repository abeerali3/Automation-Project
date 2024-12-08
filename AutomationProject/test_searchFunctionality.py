import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSearchFunctionality():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Edge()
        self.driver.set_window_size(1528, 816)

    def teardown_method(self):
        self.driver.quit()

    def perform_search(self, query):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.click()
        search_box.send_keys(query)
        search_box.send_keys(Keys.ENTER)

    def test_Incorrect_Spelling(self):
        self.driver.get("https://courses.ultimateqa.com/collections")
        self.perform_search("selenim webdriver")
        time.sleep(4)
        assert not self.driver.find_elements(By.CSS_SELECTOR, ".products__list-no-results")

    def test_search(self):
        self.driver.get("https://courses.ultimateqa.com/collections")
        self.perform_search("selenium webdriver")
        assert self.driver.find_element(By.CSS_SELECTOR, ".products__title > strong").text == "selenium webdriver"

    def test_invalid_search(self):
        self.driver.get("https://courses.ultimateqa.com/collections")
        self.perform_search("123")
        assert "No results were found" in self.driver.find_element(By.CSS_SELECTOR, ".products__list-no-results").text

    def test_search_icon(self):
        self.driver.get("https://courses.ultimateqa.com/collections")
        self.perform_search("automation")
        icon = self.driver.find_element(By.ID, "name=q")
        icon.click()
        assert self.driver.find_elements(By.CSS_SELECTOR, ".products__title")

    def test_search_and_select_product(self):
        self.driver.get("https://courses.ultimateqa.com/collections")
        self.perform_search("selenium webdriver")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".products__list-item:nth-child(2) .card__name").click()
        time.sleep(2)
        assert self.driver.find_elements(By.CSS_SELECTOR, "h2.section__heading___0cdc8")


       