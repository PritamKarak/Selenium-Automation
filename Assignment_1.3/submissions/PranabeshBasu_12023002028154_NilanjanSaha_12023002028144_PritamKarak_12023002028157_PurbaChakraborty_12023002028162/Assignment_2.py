from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browsername = "chrome"

if browsername.lower() == "chrome":
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
elif browsername.lower() == "firefox":
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )
else:
    raise Exception(
        "Invalid browser name. Please choose chrome or firefox"
    )

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# Locate all checkbox elements on the page
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(f"Total checkboxes found: {len(checkboxes)}")

# Iterate through the list of elements and interact with them
for checkbox in checkboxes:
    checkbox.click()
    assert checkbox.is_selected()
    print(f"Checkbox with value '{checkbox.get_attribute('value')}' selected: {checkbox.is_selected()}")

# Locate another set of elements (e.g., radio buttons) to inspect values
radio_buttons = driver.find_elements(By.CSS_SELECTOR, "input[name='radioButton']")
for radio in radio_buttons:
    val = radio.get_attribute("value")
    if val == "radio2":
        radio.click()
        print(f"Selected radio button: {val}")
        break

time.sleep(2)
driver.quit()
