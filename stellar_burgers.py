from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import locators as l
import pages as p
import time

class StellarBurgers():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')
        self.browser = webdriver.Chrome(options=options)
        self.browser.implicitly_wait(5)

    def __del__(self):
        self.browser.quit()

    def open_site(self, page: str):
        browser = self.browser
        browser.get(page)

    def fill_the_form(self, name: str, email: str, password: str):
        browser = self.browser
        user_data = {
            l.name_input: name,
            l.email_input: email,
            l.password_input: password
        }
        form_fields = user_data.keys()
        for field in form_fields:
            browser.find_element(By.XPATH, field).send_keys(user_data.get(field))

    def push_the_button(self, button_locator: str):
        browser = self.browser
        browser.find_element(By.XPATH, button_locator).click()

    def authorization_main(self, button: str, email: str, password: str):
        browser = self.browser
        browser.get(p.main_page)
        browser.find_element(By.XPATH, button).click()
        WebDriverWait(browser, 5).until(ec.element_to_be_clickable((By.XPATH, l.email_input_auth)))
        browser.find_element(By.XPATH, l.email_input_auth).send_keys(email)
        browser.find_element(By.XPATH, l.password_input).send_keys(password)
        browser.find_element(By.XPATH, l.enter_button).click()

    def authorization_login_page(self, button: str, email: str, password: str):
        browser = self.browser
        browser.get(p.login_page)
        browser.find_element(By.XPATH, button).click()
        browser.find_element(By.XPATH, l.enter_link).click()
        WebDriverWait(browser, 5).until(ec.element_to_be_clickable((By.XPATH, l.email_input_auth)))
        browser.find_element(By.XPATH, l.email_input_auth).send_keys(email)
        browser.find_element(By.XPATH, l.password_input).send_keys(password)
        browser.find_element(By.XPATH, l.enter_button).click()

    def get_user_info_after_auth(self):
        browser = self.browser
        browser.find_element(By.XPATH, l.user_account_button).click()
        WebDriverWait(browser, 4)
        return browser.find_element(By.XPATH, l.name_field).get_attribute('value')

    def get_reg_wrong_password_message(self):
        browser = self.browser
        return len(browser.find_elements(By.XPATH, l.reg_wrong_password_message))

    def check_url(self):
        browser = self.browser
        time.sleep(5)
        return browser.current_url

    def switch_ingredients(self, ingredient_name):
        browser = self.browser
        ingredient_locator = browser.find_element(By.XPATH, f'//h2[text()="{ingredient_name}"]')
        browser.execute_script("arguments[0].scrollIntoView();", ingredient_locator)
        WebDriverWait(browser, 3)
        return browser.find_element(By.XPATH, f'//div[span[text()="{ingredient_name}"]]').get_attribute('class')


