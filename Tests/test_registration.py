from locators import *
from generator import generate_random_email
import data_for_sb_tests as data
import urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestReg():
    def test_registration_positive_case(self, user):  # Регистрация с валидными данными (почта генерируется случайно)
        email = generate_random_email()
        password = data.valid_password
        user_data = {
            data.profile_name: RegPageStellarBurgers.name_input,
            email: RegPageStellarBurgers.email_input,
            password: RegPageStellarBurgers.password_input
        }
        form_fields = user_data.keys()
        user.get(urls.registration_page)
        for field in form_fields:
            user.find_element(*user_data.get(field)).send_keys(field)
        user.find_element(*RegPageStellarBurgers.register_button).click()
        # проверим через авторизацию по email и паролю сверкой имени
        user.get(urls.main_page)
        user.find_element(*MainPageStellarBurgers.enter_my_account_button).click()
        WebDriverWait(user, 5).until(ec.element_to_be_clickable(tuple(AuthPageStellarBurgers.email_input_auth)))
        user.find_element(*AuthPageStellarBurgers.email_input_auth).send_keys(email)
        user.find_element(*AuthPageStellarBurgers.password_input).send_keys(password)
        user.find_element(*AuthPageStellarBurgers.enter_button).click()
        user.find_element(*MainPageStellarBurgers.user_account_button).click()
        WebDriverWait(user, 4).until(ec.element_to_be_clickable(tuple(MainPageStellarBurgers.cancel_button)))
        name_to_check = user.find_element(*MainPageStellarBurgers.name_field).get_attribute('value')
        assert name_to_check == data.profile_name

    def test_registration_invalid_pwd_message(self, user):  # Слишком короткиий пароль (почта генерируется случайно)
        email = generate_random_email()
        password = data.invalid_password
        user_data = {
            data.profile_name: RegPageStellarBurgers.name_input,
            email: RegPageStellarBurgers.email_input,
            password: RegPageStellarBurgers.password_input
        }
        form_fields = user_data.keys()
        user.get(urls.registration_page)
        for field in form_fields:
            user.find_element(*user_data.get(field)).send_keys(field)
        user.find_element(*RegPageStellarBurgers.register_button).click()
        assert len(user.find_elements(*RegPageStellarBurgers.reg_wrong_password_message))
