import msvcrt
import time
from random import choice
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import variables

class CustomerJourneyBot:
    def __init__(self, use_proxy):
        # open the chrome browser and navigate to skinsfair
        service = webdriver.chrome.service.Service(variables.chrome_driver_path)
        service.start()
        if use_proxy:
            proxy = "socks5://127.0.0.1:9150"
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--proxy-server={}".format(proxy))
            self.browser = webdriver.Chrome(service=service, options=chrome_options)
        else:
            self.browser = webdriver.Chrome(service=service)
        self.browser.get(variables.skinsfair_url)
        self.browser.maximize_window()

    def login_skinsfair(self, waiting_after_login: int):
        # locate the input field and the submit button
        wait = WebDriverWait(self.browser, 2)
        input_field = wait.until(EC.visibility_of_element_located((By.ID, "password_protected_pass")))
        submit_button = wait.until(EC.visibility_of_element_located((By.ID, "wp-submit")))

        # enter password
        input_field.send_keys(variables.skinsfair_password)
        wait = WebDriverWait(self.browser, 2)

        # submit login
        submit_button.click()

        # waiting
        time.sleep(waiting_after_login)

    def activate_tracking(self, waiting_after_activate_tracking: int):
        # locate the button for activating tracking
        wait = WebDriverWait(self.browser, 2)
        accept_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cmplz-btn.cmplz-accept")))

        # click the button to accept tracking
        accept_button.click()

        # waiting
        time.sleep(waiting_after_activate_tracking)

    def select_random_tab_of_products(self, waiting_after_selecting_random_tab: int):
        # wait for the element with class eael-tabs-nav to be visible
        wait = WebDriverWait(self.browser, 2)
        tabs_nav = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "eael-tabs-nav")))

        # locate all the li elements within the div element
        tabs = self.browser.find_elements(By.CSS_SELECTOR, ".eael-tabs-nav li")

        # Randomly select one of the li elements
        random_tab = choice(tabs)

        # click the tab
        random_tab.click()

        # waiting
        time.sleep(waiting_after_selecting_random_tab)

    def select_random_product_of_tab(self, waiting_after_selecting_random_product: int):
        # locate first link
        href = self.browser.find_element(By.CLASS_NAME, "eael-tabs-content").find_element(By.CSS_SELECTOR,
                                    "div.active").find_element(By.CSS_SELECTOR, "a").get_attribute("href")

        # open the link with href
        self.browser.get(href)

        # waiting
        time.sleep(waiting_after_selecting_random_product)

    def select_random_item_in_category(self, waiting_after_selecting_random_item: int):
        # locate first link
        self.href = self.browser.find_element(By.CSS_SELECTOR, "ul.products li div a").get_attribute("href")

        # open the link with href
        self.browser.get(self.href)

        # waiting
        time.sleep(waiting_after_selecting_random_item)

    def check_item_needs_option(self, waiting_after_option_selected: int):
        # check if the href contains the words "cases" or "agenten"
        if "cases" not in self.href and "agenten" not in self.href:
            # select first option --> Zustand
            select_element = self.browser.find_element(By.ID, "zustand")
            Select(select_element).select_by_index(1)

        # waiting
        time.sleep(waiting_after_option_selected)

    def add_item_to_cart(self, waiting_after_item_added_to_cart: int):
        # Click add to cart button
        add_to_chart_button = self.browser.find_element(By.CLASS_NAME, "single_add_to_cart_button")
        add_to_chart_button.click()

        # waiting
        time.sleep(waiting_after_item_added_to_cart)

    def view_cart(self, waiting_after_visiting_cart: int):
        # go to cart
        self.browser.get("https://blog6.webcontrolling.web.prog.zone/cart/")

        # waiting
        time.sleep(waiting_after_visiting_cart)

    def click_checkout_button_in_cart(self, waiting_after_checkout: int):
        # Click checkout button
        checkout_button = self.browser.find_element(By.CLASS_NAME, "checkout-button")
        checkout_button.click()

        # waiting
        time.sleep(waiting_after_checkout)

    def fill_in_the_form(self, waiting_after_filling_form: int):
        # fill in the input fields
        values_of_ids = ['billing_first_name', 'billing_last_name', 'billing_company',
                         'billing_address_1', 'billing_address_2', 'billing_postcode', 'billing_city', 'billing_phone',
                         'billing_email', 'order_comments']
        values_to_fill = ['Auto', 'Buy', 'SkinsFair',
                          'Münzstraße 12', 'Dritter Stock --> Eye-Tracking-Labor', '97070', 'Würzburg', '0123456789',
                          'autobuy@autobuy.com', 'Dieses Produkt wurde automatisiert durch den Customer Journey Bot gekauft :)']

        counter = 0

        for id in values_of_ids:
            input_field = self.browser.find_element(By.ID, id)
            input_field.send_keys(values_to_fill[counter])
            counter += 1

        # check the AGB box
        checkbox = self.browser.find_element(By.CLASS_NAME, "input-checkbox")
        checkbox.click()

        # waiting
        time.sleep(waiting_after_filling_form)

    def click_buy_button_in_form(self, waiting_after_buying: int):
        # click buy button
        buy_button = self.browser.find_element(By.ID, "place_order")
        buy_button.click()

        # waiting
        time.sleep(waiting_after_buying)

    def close_browser(self):
        # close the browser
        self.browser.quit()

def run():
    customer_journey_bot = CustomerJourneyBot(True)
    # customer_journey_bot.login_skinsfair(3)
    customer_journey_bot.activate_tracking(3)
    customer_journey_bot.select_random_tab_of_products(3)
    customer_journey_bot.select_random_product_of_tab(3)
    customer_journey_bot.select_random_item_in_category(3)
    customer_journey_bot.check_item_needs_option(3)
    customer_journey_bot.add_item_to_cart(3)
    customer_journey_bot.view_cart(3)
    customer_journey_bot.click_checkout_button_in_cart(3)
    customer_journey_bot.fill_in_the_form(3)
    customer_journey_bot.click_buy_button_in_form(5)
    customer_journey_bot.close_browser()

if __name__ == "__main__":
    run()
