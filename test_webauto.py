from selenium import webdriver

driver = webdriver.Chrome()

def test_openGoogle():
    driver.get("https://www.google.com")
    title = driver.title

    assert title == 'Google'

def test_openFacebook():
    driver.get("https://www.facebook.com")
    title = driver.title

    assert title == 'Facebook – log in or sign up'