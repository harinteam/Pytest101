from selenium import webdriver
import pytest


driver = webdriver.Chrome()
driver.minimize_window()

alamat = [
    ("https://www.google.com", "Google"),
    ("https://www.facebook.com", "Facebook – log in or sign up")
]

@pytest.mark.parametrize('address, result', alamat)

def test_openGoogle(address, result):
    driver.get(address)
    title = driver.title

    assert title == result



