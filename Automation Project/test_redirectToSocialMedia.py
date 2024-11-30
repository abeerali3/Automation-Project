import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRedirectToSocialMedia():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Edge()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        time.sleep(timeout)  # Sleep for the timeout seconds
        new_window = [wh for wh in self.driver.window_handles if wh not in self.vars["window_handles"]]
        return new_window[0] if new_window else None

    def test_redirect_to_facebook(self):
        self._test_redirect(".et_pb_social_media_follow_network_2_tb_footer > .icon", "Ultimate QA | Saint Petersburg FL | Facebook")

    def test_redirect_to_instagram(self):
        self._test_redirect(".et_pb_social_media_follow_network_3_tb_footer > .icon", "Instagram")

    def test_redirect_to_x(self):
        self._test_redirect(".et_pb_social_media_follow_network_1_tb_footer > .icon", "X")

    def test_redirect_to_youtube(self):
        self._test_redirect(".et_pb_social_media_follow_network_4_tb_footer > .icon", "UltimateQA - YouTube", close_after=True)

    def test_redirect_to_linkedin(self):
        self._test_redirect(".et_pb_social_media_follow_network_0_tb_footer > .icon", "UltimateQA | LinkedIn")

    def _test_redirect(self, selector, expected_substring, close_after=False):
        self.driver.get("https://ultimateqa.com/automation")
        self.driver.set_window_size(1552, 832)
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.CSS_SELECTOR, selector).click()

        # Wait for new window to appear
        new_window = self.wait_for_window(2)
        if new_window:
            self.driver.switch_to.window(new_window)
            
            # Assert that the title includes the expected substring
            assert expected_substring in self.driver.title, f"Expected title to include '{expected_substring}', but got '{self.driver.title}'"
            
            if close_after:
                self.driver.close()
        else:
            pytest.fail("New window did not open.")
