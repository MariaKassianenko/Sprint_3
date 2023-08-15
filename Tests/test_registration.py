from locators import RegPageStellarBurgers as RegLoc, MainPageStellarBurgers as MainLoc, \
    AuthPageStellarBurgers as AuthLoc
from generator import generate_random_email
import data_for_sb_tests as data
import urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestReg:
    def test_registration_positive_case(self, user):
        email = generate_random_email()
        password = data.valid_password
        user_data = {
            data.profile_name: RegLoc.name_input,
            email: RegLoc.email_input,
            password: RegLoc.password_input
        }
        form_fields = user_data.keys()
        user.get(urls.registration_page)
        for field in form_fields:
            user.find_element(*user_data.get(field)).send_keys(field)
        user.find_element(*RegLoc.register_button).click()
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

    def test_registration_invalid_pwd_message(self, user):
        email = generate_random_email()
        password = data.invalid_password
        user_data = {
            data.profile_name: RegLoc.name_input,
            email: RegLoc.email_input,
            password: RegLoc.password_input
        }
        form_fields = user_data.keys()
        user.get(urls.registration_page)
        for field in form_fields:
            user.find_element(*user_data.get(field)).send_keys(field)
        user.find_element(*RegLoc.register_button).click()
        assert len(user.find_elements(*RegLoc.reg_wrong_password_message))
