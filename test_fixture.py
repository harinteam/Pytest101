# from _pytest import mark
# from _pytest.mark.structures import Mark
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

Kunci = [
    ("umarAlfatih","asDdaad0"),     # username correct password wrong
    ("umar123","asDF12#$"),         # username correct password wrong
    ("hanin", "asDG12#4")           # username wrongg password wrong
]

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/login")
    driver.minimize_window()
    driver.implicitly_wait(10)  
    yield driver
    driver.quit()

def test_login_success(setup):
    setup.find_element(By.ID, "userName").send_keys("umarAlfatih")
    setup.find_element(By.ID, "password").send_keys("asDF12#$")
    setup.find_element(By.ID, "login").click()
    time.sleep(3)

    mainHeader = setup.find_element(By.CLASS_NAME, "main-header").text

    assert mainHeader == "Profile"


@pytest.mark.parametrize('a,b', Kunci)
def test_login_failed(setup, a,b):
    setup.find_element(By.ID, "userName").send_keys(a)
    setup.find_element(By.ID, "password").send_keys(b)
    setup.find_element(By.ID, "login").click()

    invalidText = setup.find_element(By.ID, "name").text

    assert invalidText == "Invalid username or password!"

# setup.quit()