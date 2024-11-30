import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    driver = webdriver.Chrome()
    #driver = webdriver.Edge()
    driver.set_window_size(1536, 816)
    return driver

def teardown_driver(driver):
    driver.quit()

def navigate_and_assert(driver, link_text, expected_word):
    driver.get("https://ultimateqa.com/automation")
    driver.find_element(By.LINK_TEXT, link_text).click()
    time.sleep(3)  # Wait for 3 seconds after the page load
    assert expected_word.lower() in driver.title.lower(), f"Title does not contain '{expected_word}'"

def hover_and_navigate(driver, link_text, expected_word):
    driver.get("https://ultimateqa.com/automation")
    element = driver.find_element(By.LINK_TEXT, link_text)
    ActionChains(driver).move_to_element(element).perform()
    element.click()
    time.sleep(3)  # Wait for 3 seconds after the page load
    assert expected_word.lower() in driver.title.lower(), f"Title does not contain '{expected_word}'"

def test_aboutPage():
    driver = setup_driver()
    navigate_and_assert(driver, "About", "about")
    teardown_driver(driver)

def test_blogPage():
    driver = setup_driver()
    hover_and_navigate(driver, "Blog", "blog")
    teardown_driver(driver)

def test_educationPage():
    driver = setup_driver()
    driver.get("https://ultimateqa.com/automation")
    
    # Hover over the "Education" link to trigger the submenu
    education_link = driver.find_element(By.LINK_TEXT, "Education")
    ActionChains(driver).move_to_element(education_link).perform()

    sub_menu = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Free Courses"))
    )
    
    # Assert that the submenu is visible
    assert sub_menu.is_displayed(), "Submenu did not appear when hovering over 'Education'"

    # Optionally, click on the "Free Courses" link after the submenu appears
    sub_menu.click()
    time.sleep(3)  
    assert "Products" in driver.title, "Title does not contain 'Products'"
    
    teardown_driver(driver)

def test_newsletterPage():
    driver = setup_driver()
    navigate_and_assert(driver, "Newsletter", "newsletter")
    teardown_driver(driver)

def test_servicesPage():
    driver = setup_driver()
    hover_and_navigate(driver, "Services", "services")
    teardown_driver(driver)
