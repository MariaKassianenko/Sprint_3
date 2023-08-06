from stellar_burgers import StellarBurgers
import locators as l
import pytest

@pytest.fixture()
def user():
    return StellarBurgers()

@pytest.fixture()
def authorization(user):
    user.authorization_main(l.enter_my_account_button, 'mariakassianenko12013@yandex.ru', 'pwdPWD1')
