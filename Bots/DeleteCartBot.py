import msvcrt
import time
from random import choice
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import variables

class DeleteCartBot:
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

    def change_currency(self, waiting_after_changing_currency):
        skinsfair_base_link = "https://blog6.webcontrolling.web.prog.zone/"
        different_currencies = ['?currency=USD', '?currency=EUR', '?currency=BTC']
        random_currency = choice(different_currencies)
        self.browser.get(skinsfair_base_link + random_currency)
        #waiting
        time.sleep(waiting_after_changing_currency)

    def select_random_item_in_shop(self, waiting_after_selecting_random_shop_item):
        self.browser.get("https://blog6.webcontrolling.web.prog.zone/shop/")
        time.sleep(waiting_after_selecting_random_shop_item)
        shop_items = self.browser.find_elements(By.CLASS_NAME, 'product_type_variable')
        self.href = choice(shop_items).get_attribute("href")
        self.browser.get(self.href)
        time.sleep(waiting_after_selecting_random_shop_item)

    def check_item_needs_option(self, waiting_after_option_selected: int):
        # check if the href contains the words "cases" or "agenten"
        if "cases" not in self.href and "agenten" not in self.href:
            # select first option --> Zustand
            select_element = self.browser.find_element(By.ID, "zustand")
            Select(select_element).select_by_index(1)
            # select first option --> Zustand
            select_element = self.browser.find_element(By.ID, "kollektion")
            Select(select_element).select_by_index(1)
        # waiting
        time.sleep(waiting_after_option_selected)

    def add_item_to_cart(self, waiting_after_item_added_to_cart: int):
        # Click add to cart button
        add_to_chart_button = self.browser.find_element(By.CLASS_NAME, "single_add_to_cart_button")
        add_to_chart_button.click()

        # waiting
        time.sleep(waiting_after_item_added_to_cart)

    def login_my_account(self, logged_in, waiting_after_login_account):
        if logged_in:
            self.browser.get("https://blog6.webcontrolling.web.prog.zone/my-account/")
            time.sleep(waiting_after_login_account)

            # locate the input field and the submit button
            wait = WebDriverWait(self.browser, 2)
            username = wait.until(EC.visibility_of_element_located((By.ID, "username")))
            password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
            login_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "woocommerce-form-login__submit")))

            # enter password
            username.send_keys("test")
            password.send_keys("test")
            time.sleep(waiting_after_login_account)

            # submit login
            login_button.click()

            # waiting
            time.sleep(waiting_after_login_account)

    def view_cart(self, waiting_after_visiting_cart: int):
        # go to cart
        self.browser.get("https://blog6.webcontrolling.web.prog.zone/cart/")

        # waiting
        time.sleep(waiting_after_visiting_cart)

    def deleteProductInCart(self, waiting_after_deleting_product_in_cart: int):
        # Click checkout button
        delete_product_button = self.browser.find_element(By.CSS_SELECTOR, ".product-remove a")
        self.browser.get(delete_product_button.get_attribute("href"))

        # waiting
        time.sleep(waiting_after_deleting_product_in_cart)

    def close_browser(self):
        # close the browser
        self.browser.quit()

def runDeleteCartBot():
    deleteCartBot = DeleteCartBot(False)
    deleteCartBot.login_skinsfair(3)
    deleteCartBot.activate_tracking(3)
    deleteCartBot.login_my_account(False, 3)
    deleteCartBot.change_currency(5)
    deleteCartBot.select_random_item_in_shop(3)
    deleteCartBot.check_item_needs_option(3)
    deleteCartBot.add_item_to_cart(3)
    deleteCartBot.view_cart(3)
    deleteCartBot.deleteProductInCart(3)
    deleteCartBot.close_browser()

if __name__ == "__main__":
    runDeleteCartBot()
