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

# Approach 1: CSS Wildcard Selector - Starts With (^=)

radio_buttons = driver.find_elements(
    By.CSS_SELECTOR,
    "input[type='radio'][value^='radio']"
)

print("Radio buttons found using ^= :", len(radio_buttons))

radio1 = driver.find_element(
    By.CSS_SELECTOR,
    "input[type='radio'][value^='radio']"
)

radio1.click()

print("Radio1 selected using ^= selector")



# Approach 2: CSS Wildcard Selector - Contains (*=)

#radio_contains = driver.find_element(
#    By.CSS_SELECTOR,
#    "input[type='radio'][value*='adio']"
#)

#radio_contains.click()

#print("Radio button selected using *= selector")


# Approach 3: CSS Wildcard Selector - Ends With ($=)

#radio2 = driver.find_element(
#    By.CSS_SELECTOR,
#    "input[type='radio'][value$='2']"
#)

#radio2.click()

#print("Radio2 selected using $= selector")


print("CSS Wildcard Selector Test Completed Successfully")

time.sleep(5)
driver.quit()