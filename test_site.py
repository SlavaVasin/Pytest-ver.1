from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser

def test_open_s6(driver):
    driver.get('https://www.demoblaze.com/')
    galaxy_s6 = driver.find_element(By.LINK_TEXT,'Samsung galaxy s6')
    galaxy_s6.click()
    title = driver.find_element(By.CSS_SELECTOR, 'h2')
    assert title.text == 'Samsung galaxy s6'