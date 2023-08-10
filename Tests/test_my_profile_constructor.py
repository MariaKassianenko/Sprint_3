from locators import *
import data_for_sb_tests as data
import urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestTheWayFromProfileToConstuctor():
    def test_my_profile_constructor(self, user):  # переход по клику на «Конструктор»
        email = data.profile_email
        password = data.valid_password
        user.get(urls.login_page)
        WebDriverWait(user, 5).until(ec.element_to_be_clickable(tuple(AuthPageStellarBurgers.email_input_auth)))
        user.find_element(*AuthPageStellarBurgers.email_input_auth).send_keys(email)
        user.find_element(*AuthPageStellarBurgers.password_input).send_keys(password)
        user.find_element(*AuthPageStellarBurgers.enter_button).click()
        user.find_element(*MainPageStellarBurgers.user_profile_button).click()
        WebDriverWait(user, 4).until(ec.url_to_be(urls.profile_page))
        user.find_element(*MainPageStellarBurgers.constuctor_button).click()
        WebDriverWait(user, 4).until_not(ec.url_to_be(urls.profile_page))
        assert user.current_url == urls.main_page

    def test_my_profile_main_icon(self, user):  # переход по клику на логотип Stellar Burgers
        email = data.profile_email
        password = data.valid_password
        user.get(urls.login_page)
        WebDriverWait(user, 5).until(ec.element_to_be_clickable(tuple(AuthPageStellarBurgers.email_input_auth)))
        user.find_element(*AuthPageStellarBurgers.email_input_auth).send_keys(email)
        user.find_element(*AuthPageStellarBurgers.password_input).send_keys(password)
        user.find_element(*AuthPageStellarBurgers.enter_button).click()
        user.find_element(*MainPageStellarBurgers.user_profile_button).click()
        WebDriverWait(user, 4).until(ec.url_to_be(urls.profile_page))
        user.find_element(*MainPageStellarBurgers.main_icon).click()
        WebDriverWait(user, 4).until_not(ec.url_to_be(urls.profile_page))
        assert user.current_url == urls.main_page
