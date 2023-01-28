import msvcrt
import time
from random import choice
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import variables

class RandomUserClickingBot:
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
        self.browser.get("https://blog6.webcontrolling.web.prog.zone/"                      )
        counter = 0
        for counter in range(3):
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

            #increase counter
            counter+=1

        # Scroll down the entire page
        # Get the current position of the page
        current_position = self.browser.execute_script("return window.pageYOffset")
        # Get the height of the page
        page_height = self.browser.execute_script("return Math.max(document.body.scrollHeight);")

        # Scroll down the page
        for position in range(current_position, page_height, 50):
            self.browser.execute_script("window.scrollTo(0, {});".format(position))
            time.sleep(0.1)

    def change_currency(self, waiting_after_changing_currency):
        #find the change currency link and click it
        change_currency_href = self.browser.find_element(By.XPATH, '//a[text()="Zahlen Sie mit Bitcoin"]').get_attribute("href")
        self.browser.get(change_currency_href)
        #waiting
        time.sleep(waiting_after_changing_currency)
        # Scroll down the entire page
        # Get the current position of the page
        current_position = self.browser.execute_script("return window.pageYOffset")
        # Get the height of the page
        page_height = self.browser.execute_script("return Math.max(document.body.scrollHeight);")

        # Scroll down the page
        for position in range(current_position, page_height, 50):
            self.browser.execute_script("window.scrollTo(0, {});".format(position))
            time.sleep(0.1)

    def click_random_link_footer(self, waiting_after_clicking_random_footer_link):
        random_footer_hrefs = self.browser.find_elements(By.CLASS_NAME, 'wpr-no-pointer')
        random_link = choice(random_footer_hrefs).get_attribute("href")
        self.browser.get(random_link)
        time.sleep(waiting_after_clicking_random_footer_link)
        self.browser.back()
        time.sleep(waiting_after_clicking_random_footer_link)

    def click_random_social_link(self, waiting_after_clicking_random_social_link):
        random_social_hrefs = self.browser.find_elements(By.CLASS_NAME, 'elementor-social-icon')
        random_link = choice(random_social_hrefs).get_attribute("href")
        self.browser.get(random_link)
        time.sleep(waiting_after_clicking_random_social_link)
        self.browser.back()
        time.sleep(waiting_after_clicking_random_social_link)

    def click_banner_button(self, waiting_after_clicking_banner_button):
        banner_button = self.browser.find_element(By.CLASS_NAME, 'cta-button').get_attribute("href")
        self.browser.get(banner_button)
        time.sleep(waiting_after_clicking_banner_button)

    def select_random_item_in_shop(self, waiting_after_selecting_random_shop_item):
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
        # Scroll down the entire page
        # Get the current position of the page
        current_position = self.browser.execute_script("return window.pageYOffset")
        # Get the height of the page
        page_height = self.browser.execute_script("return Math.max(document.body.scrollHeight);")

        # Scroll down the page
        for position in range(current_position, page_height, 50):
            self.browser.execute_script("window.scrollTo(0, {});".format(position))
            time.sleep(0.1)
        time.sleep(waiting_after_item_added_to_cart)

    def related_products(self, waiting_after_related_product_clicked):
        random_related_products = self.browser.find_elements(By.CLASS_NAME, 'product_type_variable')
        random_link = choice(random_related_products).get_attribute("href")
        self.browser.get(random_link)
        time.sleep(waiting_after_related_product_clicked)

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

    def view_blog(self, waiting_after_watching_blog):
        self.browser.get("https://blog6.webcontrolling.web.prog.zone/blog/")
        time.sleep(waiting_after_watching_blog)

        # Scroll down the entire page
        # Get the current position of the page
        current_position = self.browser.execute_script("return window.pageYOffset")
        # Get the height of the page
        page_height = self.browser.execute_script("return Math.max(document.body.scrollHeight);")

        # Scroll down the page
        for position in range(current_position, page_height, 50):
            self.browser.execute_script("window.scrollTo(0, {});".format(position))
            time.sleep(0.1)

        # Scroll back up the page
        for position in range(page_height, current_position, -50):
            self.browser.execute_script("window.scrollTo(0, {});".format(position))
            time.sleep(0.1)

    def click_random_blog_link(self, waiting_after_clicking_random_blog_link):
        random_blog_hrefs = self.browser.find_elements(By.CSS_SELECTOR, '.elementor-widget-container a')
        random_link = ''
        while random_link == '':
            counter_strike_link = choice(random_blog_hrefs).get_attribute("href")
            if "counter-strike" in counter_strike_link:
                random_link = counter_strike_link
        self.browser.get(random_link)
        time.sleep(waiting_after_clicking_random_blog_link)
        self.browser.back()
        time.sleep(waiting_after_clicking_random_blog_link)

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
                          'autobuy@autobuy.com', 'Dieses Produkt wurde automatisiert durch den Random User Clicking Bot gekauft :)']

        counter = 0

        for id in values_of_ids:
            input_field = self.browser.find_element(By.ID, id)
            input_field.clear()
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
    randomUserClickingBot = RandomUserClickingBot(True)
    # randomUserClickingBot.login_skinsfair(3)
    randomUserClickingBot.activate_tracking(3)
    randomUserClickingBot.login_my_account(False, 3)
    randomUserClickingBot.select_random_tab_of_products(3)
    randomUserClickingBot.change_currency(5)
    randomUserClickingBot.click_random_link_footer(3)
    randomUserClickingBot.click_random_social_link(3)
    randomUserClickingBot.click_banner_button(3)
    randomUserClickingBot.select_random_item_in_shop(3)
    randomUserClickingBot.check_item_needs_option(3)
    randomUserClickingBot.add_item_to_cart(3)
    randomUserClickingBot.related_products(3)
    randomUserClickingBot.check_item_needs_option(3)
    randomUserClickingBot.add_item_to_cart(3)
    randomUserClickingBot.view_blog(3)
    randomUserClickingBot.click_random_blog_link(3)
    randomUserClickingBot.click_random_blog_link(3)
    randomUserClickingBot.view_cart(3)
    randomUserClickingBot.click_checkout_button_in_cart(3)
    randomUserClickingBot.fill_in_the_form(3)
    randomUserClickingBot.click_buy_button_in_form(5)
    randomUserClickingBot.close_browser()

if __name__ == "__main__":
    run()
