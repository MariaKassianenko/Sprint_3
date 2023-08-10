from locators import *
import data_for_sb_tests as data
import urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestLogin():
    def test_authorization_enter_my_profile_button(self, user): # Вход через кнопку Личный кабинет
        email = data.profile_email
        password = data.valid_password
        user.get(urls.main_page)
        user.find_element(*MainPageStellarBurgers.user_profile_button).click()
        WebDriverWait(user, 5).until(ec.element_to_be_clickable(tuple(AuthPageStellarBurgers.email_input_auth)))
        user.find_element(*AuthPageStellarBurgers.email_input_auth).send_keys(email)
        user.find_element(*AuthPageStellarBurgers.password_input).send_keys(password)
        user.find_element(*AuthPageStellarBurgers.enter_button).click()
        user.find_element(*MainPageStellarBurgers.user_profile_button).click()
        WebDriverWait(user, 4).until(ec.element_to_be_clickable(tuple(MainPageStellarBurgers.cancel_button)))
        name_to_check = user.find_element(*MainPageStellarBurgers.name_field).get_attribute('value')
        assert name_to_check == data.profile_name

    def test_authorization_my_account_button(self, user): # Вход через кнопку Войти в аккаунт
        email = data.profile_email
        password = data.valid_password
        user.get(urls.main_page)
        user.find_element(*MainPageStellarBurgers.enter_my_account_button).click()
        WebDriverWait(user, 5).until(ec.element_to_be_clickable(tuple(AuthPageStellarBurgers.email_input_auth)))
        user.find_element(*AuthPageStellarBurgers.email_input_auth).send_keys(email)
        user.find_element(*AuthPageStellarBurgers.password_input).send_keys(password)
        user.find_element(*AuthPageStellarBurgers.enter_button).click()
        user.find_element(*MainPageStellarBurgers.user_profile_button).click()
        WebDriverWait(user, 4).until(ec.element_to_be_clickable(tuple(MainPageStellarBurgers.cancel_button)))
        name_to_check = user.find_element(*MainPageStellarBurgers.name_field).get_attribute('value')
        assert name_to_check == data.profile_name

    def test_authorization_registration_link(self, user):  # Вход по ссылке Войти на странице Регистрации
        email = data.profile_email
        password = data.valid_password
        user.get(urls.login_page)
        user.find_element(*AuthPageStellarBurgers.registration_link).click()
        WebDriverWait(user, 5).until(ec.element_to_be_clickable(tuple(RegPageStellarBurgers.enter_link)))
        user.find_element(*RegPageStellarBurgers.enter_link).click()
        WebDriverWait(user, 5).until(ec.element_to_be_clickable(tuple(AuthPageStellarBurgers.email_input_auth)))
        user.find_element(*AuthPageStellarBurgers.email_input_auth).send_keys(email)
        user.find_element(*AuthPageStellarBurgers.password_input).send_keys(password)
        user.find_element(*AuthPageStellarBurgers.enter_button).click()
        user.find_element(*MainPageStellarBurgers.user_profile_button).click()
        WebDriverWait(user, 4).until(ec.element_to_be_clickable(tuple(MainPageStellarBurgers.cancel_button)))
        name_to_check = user.find_element(*MainPageStellarBurgers.name_field).get_attribute('value')
        assert name_to_check == data.profile_name

    def test_authorization_password_recovery_link(self, user):  # Вход по ссылке Войти на странице Восстановления пароля
        email = data.profile_email
        password = data.valid_password
        user.get(urls.login_page)
        WebDriverWait(user, 5).until(ec.element_to_be_clickable(tuple(AuthPageStellarBurgers.password_recovery_link)))
        user.find_element(*AuthPageStellarBurgers.password_recovery_link).click()
        WebDriverWait(user, 5).until(ec.element_to_be_clickable(tuple(PwdRecoveryPageStellarBurgers.enter_link)))
        user.find_element(*RegPageStellarBurgers.enter_link).click()
        WebDriverWait(user, 5).until(ec.element_to_be_clickable(tuple(AuthPageStellarBurgers.email_input_auth)))
        user.find_element(*AuthPageStellarBurgers.email_input_auth).send_keys(email)
        user.find_element(*AuthPageStellarBurgers.password_input).send_keys(password)
        user.find_element(*AuthPageStellarBurgers.enter_button).click()
        user.find_element(*MainPageStellarBurgers.user_profile_button).click()
        WebDriverWait(user, 4).until(ec.element_to_be_clickable(tuple(MainPageStellarBurgers.cancel_button)))
        name_to_check = user.find_element(*MainPageStellarBurgers.name_field).get_attribute('value')
        assert name_to_check == data.profile_name
