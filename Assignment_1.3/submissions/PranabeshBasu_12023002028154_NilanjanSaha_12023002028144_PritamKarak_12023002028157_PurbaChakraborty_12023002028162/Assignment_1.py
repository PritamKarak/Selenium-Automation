from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(2) 

#By.ID
# Action: Find the "Enter Your Name" text box and type into it
name_input = driver.find_element(By.ID, "name")
name_input.send_keys("Test User")
time.sleep(1)

# Strategy 2: By.NAME
# Action: Find the first checkbox and click it
checkbox = driver.find_element(By.NAME, "checkBoxOption1")
checkbox.click()
time.sleep(1)
# Strategy 3: By.CLASS_NAME
# Action: Find the  radio button using its class and click it

radio_btn = driver.find_element(By.CLASS_NAME, "radioButton")
radio_btn.click()
time.sleep(1)
#By.TAG_NAME
# Action: Find the static dropdown menu (which uses a <select> tag) and click it
dropdown_element = driver.find_element(By.TAG_NAME, "select")
dropdown_menu = Select(dropdown_element)
dropdown_menu.select_by_visible_text("Option2")
time.sleep(1)
#By.LINK_TEXT
# Action: Find the specific text link on the page
driver.find_element(By.LINK_TEXT, "Get Shortlisted by Recruiters - Take QA Skill Assessments on TechSmartHire").click()

time.sleep(5)
driver.quit()