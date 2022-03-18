from _pytest import mark
from _pytest.mark.structures import Mark
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

Kunci = [
    ("umarAlfatih","asDdaad0"),     # username correct password wrong
    ("umar123","asDF12#$"),       # username correct password wrong
    ("hanin", "asDG12#4")           # username wrongg password wrong
]

driver = webdriver.Chrome()
driver.minimize_window()
driver.implicitly_wait(10)

def test_login_success():
    driver.get("https://demoqa.com/login")
    driver.find_element(By.ID, "userName").send_keys("umarAlfatih")
    driver.find_element(By.ID, "password").send_keys("asDF12#$")
    driver.find_element(By.ID, "login").click()

@pytest.mark.parametrize('a,b', Kunci)
def test_login_failed(a,b):
    driver.get("https://demoqa.com/login")
    driver.find_element(By.ID, "userName").send_keys(a)
    driver.find_element(By.ID, "password").send_keys(b)
    driver.find_element(By.ID, "login").click()

    invalidText = driver.find_element(By.ID, "name").text

    assert invalidText == "Invalid username or password!"