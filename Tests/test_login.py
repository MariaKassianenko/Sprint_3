import locators as l


def test_authorization_enter_my_account_button(user):
    user.authorization_main(l.enter_my_account_button, 'mariakassianenko12013@yandex.ru', 'pwdPWD1')
    assert user.get_user_info_after_auth() == 'Мария'


def test_authorization_my_account_button(user):
    user.authorization_main(l.enter_my_account_button, 'mariakassianenko12013@yandex.ru', 'pwdPWD1')
    assert user.get_user_info_after_auth() == 'Мария'


def test_authorization_registration_link(user):
    user.authorization_login_page(l.registration_link, 'mariakassianenko12013@yandex.ru', 'pwdPWD1')
    assert user.get_user_info_after_auth() == 'Мария'


def test_authorization_password_recovery_link(user):
    user.authorization_login_page(l.password_recovery_link, 'mariakassianenko12013@yandex.ru', 'pwdPWD1')
    assert user.get_user_info_after_auth() == 'Мария'
