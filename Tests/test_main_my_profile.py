from locators import *
import data_for_sb_tests as data
import urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestMyProfile():
    def test_main_my_profile(self, user):  # переход по клику на «Личный кабинет»
        email = data.profile_email
        password = data.valid_password
        user.get(urls.main_page)
        user.find_element(*MainPageStellarBurgers.user_profile_button).click()
        WebDriverWait(user, 5).until(ec.element_to_be_clickable(tuple(AuthPageStellarBurgers.email_input_auth)))
        user.find_element(*AuthPageStellarBurgers.email_input_auth).send_keys(email)
        user.find_element(*AuthPageStellarBurgers.password_input).send_keys(password)
        user.find_element(*AuthPageStellarBurgers.enter_button).click()
        WebDriverWait(user, 4).until(ec.url_to_be(urls.main_page))
        user.find_element(*MainPageStellarBurgers.user_profile_button).click()
        WebDriverWait(user, 4).until(ec.element_to_be_clickable(tuple(MainPageStellarBurgers.cancel_button)))
        assert user.current_url == urls.profile_page
