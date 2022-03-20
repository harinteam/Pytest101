from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

Kunci = [
    ("umarAlfatih","asDdaad0"),     # username correct password wrong
    ("umar123","asDF12#$"),         # username correct password wrong
    ("hanin", "asDG12#4")           # username wrongg password wrong
]

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging']) 


# ==========================
# FIXTURE
# ==========================
@pytest.fixture
def setup():
    driver = webdriver.Chrome(options=options)
    driver.get("https://demoqa.com/login")
    driver.minimize_window()
    driver.implicitly_wait(10)  
    yield driver
    driver.quit()

    

# =========================================================================
# SCENARIO / TESTCASE 1 : LOGIN WITH CORRECT USERNAME AND CORRECT PASSWORD
# =========================================================================

@pytest.mark.positivetest
def test_login_success(setup):
    setup.find_element(By.ID, "userName").send_keys("umarAlfatih")
    setup.find_element(By.ID, "password").send_keys("asDF12#$")
    setup.find_element(By.ID, "login").click()
    

    userName = setup.find_element(By.ID, "userName-value").text

    assert userName == "umaralfatih"

# ============================================================================
# SCENARIO / TESTCASE 2-3-4 : LOGIN WITH INPUT COMBINATION CONTAIN WRONG VALUE
# ============================================================================

@pytest.mark.negativetest
@pytest.mark.parametrize('a,b', Kunci)
def test_login_failed(setup, a,b):
    setup.find_element(By.ID, "userName").send_keys(a)
    setup.find_element(By.ID, "password").send_keys(b)
    setup.find_element(By.ID, "login").click()

    invalidText = setup.find_element(By.ID, "name").text

    assert invalidText == "Invalid username or password!"

