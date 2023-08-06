import locators as l
import pages as p


def test_registration_positive_case(user):
    user.open_site(p.registration_page)
    user.fill_the_form('Мария', 'mariakassianenko12013@yandex.ru', 'pwdPWD1')
    user.push_the_button(l.register_button)
    email = 'mariakassianenko12012@yandex.ru'
    password = 'pwdPWD1'
    user.authorization_main(l.enter_my_account_button, email, password)
    assert user.get_user_info_after_auth() == 'Мария'


def test_registration_wrong_password_message(user):
    user.open_site(p.registration_page)
    user.fill_the_form('Мария', 'mariakassianenko12011@yandex.ru', '12345')
    user.push_the_button(l.register_button)
    assert user.get_reg_wrong_password_message()
