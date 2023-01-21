import msvcrt
import time
from random import choice
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# open the chrome browser and navigate to skinsfair
service = webdriver.chrome.service.Service()
service.start()
browser = webdriver.Chrome(service=service)
browser.get()

# waiting
time.sleep(10)

# create a new browser instance
browser = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

# Maximize the browser window
browser.maximize_window()

# waiting
time.sleep(100)

# locate the input field and the submit button
wait = WebDriverWait(browser, 2)
input_field = wait.until(EC.visibility_of_element_located((By.ID, "password_protected_pass")))
submit_button = wait.until(EC.visibility_of_element_located((By.ID, "wp-submit")))

# enter password
input_field.send_keys()
wait = WebDriverWait(browser, 2)

# submit login
submit_button.click()

# waiting
time.sleep(3)

# locate the button for activating tracking
wait = WebDriverWait(browser, 2)
accept_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cmplz-btn.cmplz-accept")))

# click the button to accept tracking
accept_button.click()

# waiting
time.sleep(3)

# wait for the element with class eael-tabs-nav to be visible
wait = WebDriverWait(browser, 2)
tabs_nav = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "eael-tabs-nav")))

# locate all the li elements within the div element
tabs = browser.find_elements(By.CSS_SELECTOR, ".eael-tabs-nav li")

# Randomly select one of the li elements
random_tab = choice(tabs)

# click the tab
random_tab.click()

# waiting
time.sleep(3)

# locate first link
href = browser.find_element(By.CLASS_NAME, "eael-tabs-content").find_element(By.CSS_SELECTOR,
                            "div.active").find_element(By.CSS_SELECTOR, "a").get_attribute("href")

# open the link with href
browser.get(href)

# waiting
time.sleep(3)

# locate first link
href = browser.find_element(By.CSS_SELECTOR, "ul.products li div a").get_attribute("href")

# open the link with href
browser.get(href)

# locate first link
href = browser.find_element(By.CSS_SELECTOR, "ul.products li div a").get_attribute("href")

# waiting
time.sleep(5)

# check if the href contains the words "cases" or "agenten"
if "cases" not in href and "agenten" not in href:
    # select first option
    select_element = browser.find_element(By.CLASS_NAME, "variations").find_element(By.TAG_NAME, "tbody").find_element(
        By.TAG_NAME, "tr").find_element(By.TAG_NAME, "td").find_element(By.TAG_NAME, "select")
    Select(select_element).select_by_index(1)

# waiting
time.sleep(5)

# Click add to chart button
add_to_chart_button = browser.find_element(By.CLASS_NAME, "single_add_to_cart_button")
add_to_chart_button.click()

# waiting
time.sleep(3)

# go to cart
browser.get("https://blog6.webcontrolling.web.prog.zone/cart/")

# waiting
time.sleep(3)

# Click checkout button
checkout_button = browser.find_element(By.CLASS_NAME, "checkout-button")
checkout_button.click()

# waiting
time.sleep(3)

# fill in the input fields
values_of_ids = ['billing_first_name', 'billing_last_name', 'billing_company',
                 'billing_address_1', 'billing_address_2', 'billing_postcode', 'billing_city', 'billing_phone',
                 'billing_email', 'order_comments']
values_to_fill = ['Auto', 'Buy', 'SkinsFair',
                  'Münzstraße 12', 'Dritter Stock --> Eye-Tracking-Labor', '97070', 'Würzburg', '0123456789',
                  'autobuy@autobuy.com', 'Dieses Produkt wurde automatisiert gekauft :)']

counter = 0

for id in values_of_ids:
    input_field = browser.find_element(By.ID, id)
    input_field.send_keys(values_to_fill[counter])
    counter += 1

# check the AGB box
checkbox = browser.find_element(By.CLASS_NAME, "input-checkbox")
checkbox.click()

# waiting
time.sleep(3)

# click buy button
buy_button = browser.find_element(By.ID, "place_order")
buy_button.click()

# waiting
time.sleep(8)

# close the browser
browser.quit()
