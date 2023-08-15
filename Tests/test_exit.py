from locators import AuthPageStellarBurgers as AuthLoc, MainPageStellarBurgers as MainLoc
import data_for_sb_tests as data
import urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestExitProfile:
    def test_exit_profile(self, user):
        email = data.profile_email
        password = data.valid_password
        user.get(urls.login_page)
        WebDriverWait(user, 5).until(ec.element_to_be_clickable(tuple(AuthLoc.email_input_auth)))
        user.find_element(*AuthLoc.email_input_auth).send_keys(email)
        user.find_element(*AuthLoc.password_input).send_keys(password)
        user.find_element(*AuthLoc.enter_button).click()
        user.find_element(*MainLoc.user_profile_button).click()
        WebDriverWait(user, 5).until(ec.element_to_be_clickable(tuple(MainLoc.exit_button)))
        user.find_element(*MainLoc.exit_button).click()
        WebDriverWait(user, 5).until_not(ec.url_to_be(urls.profile_page))
        assert user.current_url == urls.login_page
