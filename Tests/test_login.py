from locators import AuthPageStellarBurgers as AuthLoc, MainPageStellarBurgers as MainLoc, \
    RegPageStellarBurgers as RegLoc, PwdRecoveryPageStellarBurgers as PwdRecLoc
import data_for_sb_tests as data
import urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestLogin:
    def test_authorization_enter_my_profile_button(self, user):
        email = data.profile_email
        password = data.valid_password
        user.get(urls.main_page)
        user.find_element(*MainLoc.user_profile_button).click()
        WebDriverWait(user, 5).until(ec.element_to_be_clickable(tuple(AuthLoc.email_input_auth)))
        user.find_element(*AuthLoc.email_input_auth).send_keys(email)
        user.find_element(*AuthLoc.password_input).send_keys(password)
        user.find_element(*AuthLoc.enter_button).click()
        user.find_element(*MainLoc.user_profile_button).click()
        WebDriverWait(user, 5).until(ec.element_to_be_clickable(tuple(MainLoc.cancel_button)))
        name_to_check = user.find_element(*MainLoc.name_field).get_attribute('value')
        assert name_to_check == data.profile_name

    def test_authorization_my_account_button(self, user):
        email = data.profile_email
        password = data.valid_password
        user.get(urls.main_page)
        user.find_element(*MainLoc.enter_my_account_button).click()
        WebDriverWait(user, 5).until(ec.element_to_be_clickable(tuple(AuthLoc.email_input_auth)))
        user.find_element(*AuthLoc.email_input_auth).send_keys(email)
        user.find_element(*AuthLoc.password_input).send_keys(password)
        user.find_element(*AuthLoc.enter_button).click()
        user.find_element(*MainLoc.user_profile_button).click()
        WebDriverWait(user, 5).until(ec.element_to_be_clickable(tuple(MainLoc.cancel_button)))
        name_to_check = user.find_element(*MainLoc.name_field).get_attribute('value')
        assert name_to_check == data.profile_name

    def test_authorization_registration_link(self, user):
        email = data.profile_email
        password = data.valid_password
        user.get(urls.login_page)
        user.find_element(*AuthLoc.registration_link).click()
        WebDriverWait(user, 5).until(ec.element_to_be_clickable(tuple(RegLoc.enter_link)))
        user.find_element(*RegLoc.enter_link).click()
        WebDriverWait(user, 5).until(ec.element_to_be_clickable(tuple(AuthLoc.email_input_auth)))
        user.find_element(*AuthLoc.email_input_auth).send_keys(email)
        user.find_element(*AuthLoc.password_input).send_keys(password)
        user.find_element(*AuthLoc.enter_button).click()
        user.find_element(*MainLoc.user_profile_button).click()
        WebDriverWait(user, 5).until(ec.element_to_be_clickable(tuple(MainLoc.cancel_button)))
        name_to_check = user.find_element(*MainLoc.name_field).get_attribute('value')
        assert name_to_check == data.profile_name

    def test_authorization_password_recovery_link(self, user):
        email = data.profile_email
        password = data.valid_password
        user.get(urls.login_page)
        WebDriverWait(user, 5).until(ec.element_to_be_clickable(tuple(AuthLoc.password_recovery_link)))
        user.find_element(*AuthLoc.password_recovery_link).click()
        WebDriverWait(user, 5).until(ec.element_to_be_clickable(tuple(PwdRecLoc.enter_link)))
        user.find_element(*RegLoc.enter_link).click()
        WebDriverWait(user, 5).until(ec.element_to_be_clickable(tuple(AuthLoc.email_input_auth)))
        user.find_element(*AuthLoc.email_input_auth).send_keys(email)
        user.find_element(*AuthLoc.password_input).send_keys(password)
        user.find_element(*AuthLoc.enter_button).click()
        user.find_element(*MainLoc.user_profile_button).click()
        WebDriverWait(user, 5).until(ec.element_to_be_clickable(tuple(MainLoc.cancel_button)))
        name_to_check = user.find_element(*MainLoc.name_field).get_attribute('value')
        assert name_to_check == data.profile_name
