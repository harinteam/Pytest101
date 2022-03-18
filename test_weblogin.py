from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

Kunci = [
    ("umarAlfatih","asDF12#$"),     # username correct passwor correct
    ("umarAlfatih","okeoke"),       # username correct passwor wrong
    ("hanin", "asDG12#4")           # username worng passwor correct
]

driver = webdriver.Chrome()
driver.minimize_window()
driver.implicitly_wait(10)

@pytest.mark.parametrize('a, b', Kunci)
def test_login(a,b):
    driver.get("https://demoqa.com/login")
    driver.find_element(By.ID, "userName").send_keys(a)
    driver.find_element(By.ID, "password").send_keys(b)
    driver.find_element(By.ID, "login").click()

    invalidText = driver.find_element(By.ID, "name").text

    assert invalidText == "Invalid username or password!"