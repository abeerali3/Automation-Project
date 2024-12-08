import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAutomation:
    def setup_driver(self):
        """Setup WebDriver."""
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1536, 816)

    def teardown_driver(self):
        """Teardown WebDriver."""
        if self.driver:
            self.driver.quit()

    def navigate_and_assert(self, link_text, expected_word):
        """Navigate to the page and assert the title contains the expected word."""
        self.driver.get("https://ultimateqa.com/automation")
        self.driver.find_element(By.LINK_TEXT, link_text).click()
        time.sleep(3)
        assert expected_word.lower() in self.driver.title.lower(), f"Title does not contain '{expected_word}'"

    def hover_and_navigate(self, link_text, expected_word):
        """Hover over a link, click it, and assert the title."""
        self.driver.get("https://ultimateqa.com/automation")
        element = self.driver.find_element(By.LINK_TEXT, link_text)
        ActionChains(self.driver).move_to_element(element).perform()
        element.click()
        time.sleep(3)
        assert expected_word.lower() in self.driver.title.lower(), f"Title does not contain '{expected_word}'"

    def hover_and_assert_submenu(self, link_text, submenu_text, expected_word):
        """Hover over a link to display the submenu and assert the title."""
        self.driver.get("https://ultimateqa.com/automation")
        element = self.driver.find_element(By.LINK_TEXT, link_text)
        ActionChains(self.driver).move_to_element(element).perform()

        # Wait for the submenu to be visible
        sub_menu = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.LINK_TEXT, submenu_text))
        )

        # First step: Check if the submenu is displayed (just a check, no assertion for failure)
        if sub_menu.is_displayed():
            print(f"Submenu '{submenu_text}' is displayed.")
        else:
            print(f"Submenu '{submenu_text}' is NOT displayed when hovering over '{link_text}'")
        
        # Proceed with clicking the submenu and checking the title
        sub_menu.click()
        time.sleep(3)

        # Second assert: Check if the title contains the expected word
        assert expected_word in self.driver.title, f"Title does not contain '{expected_word}'"


# Test cases
class TestPages:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Fixture to handle setup and teardown."""
        self.test_automation = TestAutomation()
        self.test_automation.setup_driver()
        yield
        self.test_automation.teardown_driver()

    def test_about_page(self):
        self.test_automation.navigate_and_assert("About", "about")

    def test_blog_page(self):
        self.test_automation.hover_and_navigate("Blog", "blog")

    def test_education_page(self):
        self.test_automation.hover_and_assert_submenu("Education", "Free Courses", "Products")

    def test_newsletter_page(self):
        self.test_automation.navigate_and_assert("Newsletter", "newsletter")

    def test_services_page(self):
        self.test_automation.hover_and_navigate("Services", "services")
